from __future__ import annotations
import flet as ft
import re
from typing import Union, List, Dict, Optional, cast
from dataclasses import dataclass
from functools import lru_cache

@dataclass
class DStringConfig:
    """Configuration for DString parsing and rendering"""

    default_color: str = ft.Colors.AMBER
    default_size: int = 14
    pattern: str = r"d\[<(.*?)>, <(.*?)>\]"


class DStringError(Exception):
    """Base exception for DString-related errors"""

    pass


class DStringParseError(DStringError):
    """Raised when parsing a DString fails"""

    pass


class DStringStyleError(DStringError):
    """Raised when creating a text style fails"""

    pass


class DString:
    """
    DString (Dynamic String) provides a simple syntax for creating richly styled text in Flet applications.

    Example:
        ```python
        import flet as ft
        from flet.dstring import DString

        # Create styled text
        styled_text = "d[<f=ff6b6b,b>, <Hello>] d[<f=4ecdc4,i>, <World>]"
        text = DString(styled_text).to_flet()

        # Add to page
        page.add(text)
        ```

    Syntax:
        - Basic format: d[<style_params>, <text>]
        - Multiple styles can be combined with commas
        - Available style parameters:
            f=XXXXXX : Foreground color (hex)
            b=XXXXXX : Background color (hex)
            dc=XXXXXX : Decoration color (hex)
            gs=XXXXXX : Gradient start color (hex)
            ge=XXXXXX : Gradient end color (hex)
            size=N : Font size (integer)
            ff=name : Font family
            h=N : Height (float)
            ls=N : Letter spacing (float)
            ws=N : Word spacing (float)
            dt=N : Decoration thickness (float)
            ds=style : Decoration style (solid|double|dotted|dashed|wavy)
            d=type : Decoration type (underline|overline|line-through)
            bl=type : Baseline (alphabetic|ideographic)
            o=type : Overflow (clip|ellipsis|fade|visible)
            w=weight : Font weight (normal|bold|w100-w900)
            shadow=color,x,y,blur,spread : Box shadow
            i : Italic
            u : Underline
            b : Bold
    """

    def __init__(self, text: str, config: Optional[DStringConfig] = None):
        self.text = text
        self.config = config or DStringConfig()
        self._pattern = re.compile(self.config.pattern)
        self._spans: Optional[List[ft.TextSpan]] = None
        self._style_maps = self._create_style_maps()

    @staticmethod
    def _interpolate_color(self, start_hex: str, end_hex: str, steps: int) -> List[str]:
        """Interpolate between two hex colors"""

        def hex_to_rgb(hex_str: str) -> tuple[int, int, int]:
            return (int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:6], 16))

        def rgb_to_hex(r: int, g: int, b: int) -> str:
            return f"{r:02x}{g:02x}{b:02x}"

        start_rgb = hex_to_rgb(start_hex)
        end_rgb = hex_to_rgb(end_hex)
        colors = []

        for i in range(steps):
            ratio = i / (steps - 1) if steps > 1 else 0
            r = round(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * ratio)
            g = round(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * ratio)
            b = round(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * ratio)
            colors.append(rgb_to_hex(r, g, b))

        return colors

    @staticmethod
    def _create_style_maps() -> Dict:
        """Create static style mapping dictionaries"""
        return {
            "decoration": {
                "underline": ft.TextDecoration.UNDERLINE,
                "overline": ft.TextDecoration.OVERLINE,
                "line-through": ft.TextDecoration.LINE_THROUGH,
            },
            "decoration_style": {
                "solid": ft.TextDecorationStyle.SOLID,
                "double": ft.TextDecorationStyle.DOUBLE,
                "dotted": ft.TextDecorationStyle.DOTTED,
                "dashed": ft.TextDecorationStyle.DASHED,
                "wavy": ft.TextDecorationStyle.WAVY,
            },
            "baseline": {
                "alphabetic": ft.TextBaseline.ALPHABETIC,
                "ideographic": ft.TextBaseline.IDEOGRAPHIC,
            },
            "overflow": {
                "clip": ft.TextOverflow.CLIP,
                "ellipsis": ft.TextOverflow.ELLIPSIS,
                "fade": ft.TextOverflow.FADE,
                "visible": ft.TextOverflow.VISIBLE,
            },
            "weight": {
                "normal": ft.FontWeight.NORMAL,
                "bold": ft.FontWeight.BOLD,
                "w100": ft.FontWeight.W_100,
                "w200": ft.FontWeight.W_200,
                "w300": ft.FontWeight.W_300,
                "w400": ft.FontWeight.W_400,
                "w500": ft.FontWeight.W_500,
                "w600": ft.FontWeight.W_600,
                "w700": ft.FontWeight.W_700,
                "w800": ft.FontWeight.W_800,
                "w900": ft.FontWeight.W_900,
            },
        }

    @staticmethod
    @lru_cache(maxsize=128)
    def _is_valid_hex(hex_color: str) -> bool:
        """Validate hex color strings"""
        return bool(re.match(r"^[0-9A-Fa-f]{6}$", hex_color))

    @staticmethod
    @lru_cache(maxsize=128)
    def _is_valid_float(value: str) -> bool:
        """Validate float strings"""
        return bool(re.match(r"^-?\d*\.?\d+$", value))

    def _parse_shadow(self, shadow_str: str) -> Optional[ft.BoxShadow]:
        """Parse shadow string in format 'color,offset_x,offset_y,blur_radius,spread_radius'"""
        try:
            color, offset_x, offset_y, blur_radius, spread_radius = shadow_str.split(
                ","
            )
            if not self._is_valid_hex(color):
                return None
            return ft.BoxShadow(
                color=f"#{color}",
                offset_x=float(offset_x),
                offset_y=float(offset_y),
                blur_radius=float(blur_radius),
                spread_radius=float(spread_radius),
            )
        except:
            return None

    def _parse_style_params(self, params_str: str) -> Dict:
        """Parse style parameters from string format into dictionary"""
        style_dict = {
            "italic": False,
            "underline": False,
            "bold": False,
            "size": self.config.default_size,
            "font_family": None,
            "foreground": None,
            "background": None,
            "decoration_color": None,
            "height": None,
            "letter_spacing": None,
            "word_spacing": None,
            "decoration": None,
            "decoration_style": None,
            "decoration_thickness": None,
            "baseline": None,
            "shadow": None,
            "overflow": None,
            "gradient_start": None,
            "gradient_end": None,
        }

        parts = params_str.split(",")
        for part in parts:
            if "=" in part:
                name, value = part.split("=", 1)
                name, value = name.strip(), value.strip()

                if name == "f" and self._is_valid_hex(value):
                    style_dict["foreground"] = value
                elif name == "b" and self._is_valid_hex(value):
                    style_dict["background"] = value
                elif name == "dc" and self._is_valid_hex(value):
                    style_dict["decoration_color"] = value
                elif name == "size" and value.isdigit():
                    style_dict["size"] = int(value)
                elif name == "ff":
                    style_dict["font_family"] = value
                elif name == "h" and self._is_valid_float(value):
                    style_dict["height"] = float(value)
                elif name == "ls" and self._is_valid_float(value):
                    style_dict["letter_spacing"] = float(value)
                elif name == "ws" and self._is_valid_float(value):
                    style_dict["word_spacing"] = float(value)
                elif name == "dt" and self._is_valid_float(value):
                    style_dict["decoration_thickness"] = float(value)
                elif name == "ds" and value in self._style_maps["decoration_style"]:
                    style_dict["decoration_style"] = value
                elif name == "d" and value in self._style_maps["decoration"]:
                    style_dict["decoration"] = value
                elif name == "bl" and value in self._style_maps["baseline"]:
                    style_dict["baseline"] = value
                elif name == "o" and value in self._style_maps["overflow"]:
                    style_dict["overflow"] = value
                elif name == "w" and value in self._style_maps["weight"]:
                    style_dict["bold"] = value
                elif name == "shadow":
                    style_dict["shadow"] = self._parse_shadow(value)
                elif name == "gs" and self._is_valid_hex(value):
                    style_dict["gradient_start"] = value
                elif name == "ge" and self._is_valid_hex(value):
                    style_dict["gradient_end"] = value
            else:
                part = part.strip()
                style_dict["italic"] |= "i" in part
                style_dict["underline"] |= "u" in part
                style_dict["bold"] |= "b" in part

        return style_dict

    def _create_gradient_spans(self, text: str, style_dict: Dict) -> List[ft.TextSpan]:
        """Create a list of spans for gradient text"""
        if not (style_dict.get("gradient_start") and style_dict.get("gradient_end")):
            return [ft.TextSpan(text=text, style=self._create_text_style(style_dict))]

        start = style_dict["gradient_start"]
        end = style_dict["gradient_end"]
        spans = []

        for i, char in enumerate(text):
            ratio = i / (len(text) - 1) if len(text) > 1 else 0
            r = round(
                int(start[0:2], 16) + (int(end[0:2], 16) - int(start[0:2], 16)) * ratio
            )
            g = round(
                int(start[2:4], 16) + (int(end[2:4], 16) - int(start[2:4], 16)) * ratio
            )
            b = round(
                int(start[4:6], 16) + (int(end[4:6], 16) - int(start[4:6], 16)) * ratio
            )
            color = f"#{r:02x}{g:02x}{b:02x}"

            style = ft.TextStyle(
                color=color, size=style_dict.get("size", self.config.default_size)
            )
            spans.append(ft.TextSpan(text=char, style=style))

        return spans

    def _create_text_style(self, style_dict: Dict) -> ft.TextStyle:
        """Create Flet TextStyle from style dictionary"""
        try:
            if style_dict.get("foreground"):
                color = f"#{style_dict['foreground']}"
            else:
                color = self.config.default_color
            style = ft.TextStyle(
                color=color,
                size=style_dict.get("size", self.config.default_size),
            )

            if style_dict.get("background"):
                style.bgcolor = f"#{style_dict['background']}"
            if style_dict.get("italic"):
                style.italic = True
            if isinstance(style_dict.get("bold"), str):
                style.weight = self._style_maps["weight"][style_dict["bold"]]
            elif style_dict.get("bold"):
                style.weight = ft.FontWeight.BOLD

            if style_dict.get("decoration"):
                style.decoration = self._style_maps["decoration"][
                    style_dict["decoration"]
                ]
            if style_dict.get("decoration_style"):
                style.decoration_style = self._style_maps["decoration_style"][
                    style_dict["decoration_style"]
                ]
            if style_dict.get("decoration_color"):
                style.decoration_color = f"#{style_dict['decoration_color']}"
            if style_dict.get("decoration_thickness"):
                style.decoration_thickness = style_dict["decoration_thickness"]

            if style_dict.get("font_family"):
                style.font_family = style_dict["font_family"]
            if style_dict.get("height"):
                style.height = style_dict["height"]
            if style_dict.get("letter_spacing"):
                style.letter_spacing = style_dict["letter_spacing"]
            if style_dict.get("word_spacing"):
                style.word_spacing = style_dict["word_spacing"]
            if style_dict.get("baseline"):
                style.baseline = self._style_maps["baseline"][style_dict["baseline"]]
            if style_dict.get("overflow"):
                style.overflow = self._style_maps["overflow"][style_dict["overflow"]]
            if style_dict.get("shadow"):
                style.shadow = [style_dict["shadow"]]

            return style
        except Exception as e:
            raise DStringStyleError(f"Failed to create text style: {str(e)}")

    def to_spans(self) -> List[ft.TextSpan]:
        """Convert DString to list of TextSpans"""
        if self._spans is not None:
            return self._spans

        spans = []
        current_pos = 0
        default_style = ft.TextStyle(
            color=self.config.default_color, size=self.config.default_size
        )

        for match in self._pattern.finditer(self.text):
            if match.start() > current_pos:
                plain_text = self.text[current_pos : match.start()]
                spans.append(ft.TextSpan(text=plain_text, style=default_style))

            try:
                style_params, text = match.groups()
                style_dict = self._parse_style_params(style_params)

                spans.extend(self._create_gradient_spans(text, style_dict))

            except Exception as e:
                raise DStringParseError(
                    f"Failed to parse style at position {match.start()}: {str(e)}"
                )

            current_pos = match.end()

        if current_pos < len(self.text):
            spans.append(ft.TextSpan(text=self.text[current_pos:], style=default_style))

        self._spans = spans
        return spans

    def to_flet(self) -> ft.Text:
        """Convert DString to Flet Text control"""
        try:
            return ft.Text(spans=self.to_spans())
        except Exception as e:
            raise DStringError(f"Failed to create Flet Text: {str(e)}")


DEFAULT_STYLE = ft.TextStyle(color=ft.Colors.AMBER, size=14)


def create_demo_page(page: ft.Page):
    """Create a demo page showing DString capabilities"""

    page.title = "DString Demo"
    page.add(ft.Text("DString Styling Demo", size=32, weight=ft.FontWeight.BOLD))

    # Basic Styling Demo
    basic_demo = (
        "Basic styling: "
        "d[<f=ff6b6b,b>, <bold>], "
        "d[<f=4ecdc4,i>, <italic>], "
        "d[<f=45b7d1,u>, <underlined>]"
    )
    page.add(
        ft.Text("Basic Styling", size=24, weight=ft.FontWeight.BOLD),
        DString(basic_demo).to_flet(),
    )

    # Colors and Sizes Demo
    Colors_demo = (
        "Colors and sizes: "
        "d[<f=ff0000,size=20>, <Red and Big>], "
        "d[<f=00ff00,size=16>, <Green and Medium>], "
        "d[<f=0000ff,size=12>, <Blue and Small>]"
    )
    page.add(
        ft.Text("Colors and Sizes", size=24, weight=ft.FontWeight.BOLD),
        DString(Colors_demo).to_flet(),
    )

    # Font Styles Demo
    fonts_demo = (
        "Font styles: "
        "d[<ff=Arial>, <Arial>], "
        "d[<ff=Courier New>, <Courier New>], "
        "d[<ff=Times New Roman>, <Times New Roman>]"
    )
    page.add(
        ft.Text("Font Families", size=24, weight=ft.FontWeight.BOLD),
        DString(fonts_demo).to_flet(),
    )

    # Text Decorations Demo
    decorations_demo = (
        "Text decorations: "
        "d[<d=underline,ds=solid,dc=ff0000>, <Solid Underline>], "
        "d[<d=overline,ds=dotted,dc=00ff00>, <Dotted Overline>], "
        "d[<d=line-through,ds=wavy,dc=0000ff>, <Wavy Strikethrough>]"
    )
    page.add(
        ft.Text("Text Decorations", size=24, weight=ft.FontWeight.BOLD),
        DString(decorations_demo).to_flet(),
    )

    # Spacing Demo
    spacing_demo = (
        "Spacing controls: "
        "d[<ls=2>, <L e t t e r   S p a c i n g>], "
        "d[<ws=10>, <Word Spacing Example>]"
    )
    page.add(
        ft.Text("Spacing Controls", size=24, weight=ft.FontWeight.BOLD),
        DString(spacing_demo).to_flet(),
    )

    # Shadows Demo
    shadows_demo = (
        "Text shadows: "
        "d[<f=ff0000,shadow=000000,2,2,4,0>, <Red with Shadow>], "
        "d[<f=00ff00,shadow=ff0000,2,2,4,0>, <Green with Red Shadow>]"
    )
    page.add(
        ft.Text("Text Shadows", size=24, weight=ft.FontWeight.BOLD),
        DString(shadows_demo).to_flet(),
    )

    # Text Overflow Demo
    overflow_demo = (
        "Overflow handling: "
        "d[<o=clip,b=000000>, <This text will be clipped at the boundary...>], "
        "d[<o=ellipsis,b=000000>, <This text will show ellipsis...>], "
        "d[<o=fade,b=000000>, <This text will fade out at the edge...>]"
    )
    page.add(
        ft.Text("Text Overflow", size=24, weight=ft.FontWeight.BOLD),
        DString(overflow_demo).to_flet(),
    )

    # Font Weights Demo
    weights_demo = (
        "Font weights: "
        "d[<w=w100>, <Thin>], "
        "d[<w=w400>, <Regular>], "
        "d[<w=w700>, <Bold>], "
        "d[<w=w900>, <Black>]"
    )
    page.add(
        ft.Text("Font Weights", size=24, weight=ft.FontWeight.BOLD),
        DString(weights_demo).to_flet(),
    )

    # Complex Demo
    complex_demo = (
        "d[<f=ff6b6b,w=bold,size=32,b=000000>, <Welcome>] to the "
        "d[<f=4ecdc4,i,ff=Arial>, <Extended>] "
        "d[<f=45b7d1,d=underline,ds=wavy,dc=ff0000>, <Styling>] "
        "d[<f=96ceb4,h=1.5>, <System>]!\n\n"
        "Now with d[<f=ff0000,ls=2>, <l e t t e r   s p a c i n g>] and "
        "d[<f=00ff00,ws=10>, <word spacing>] control.\n\n"
        "Add some d[<f=ffd700,shadow=ff0000,2,2,4,0>, <dynamic shadows>] and "
        "d[<f=ffffff,b=000000,o=ellipsis>, <text overflow control...>]\n\n"
        "Mix d[<f=ff69b4,d=line-through,ds=dotted>, <different>] "
        "d[<f=4ecdc4,d=overline,ds=dashed>, <text>] "
        "d[<f=ffd700,d=underline,ds=double>, <decorations>]!\n\n"
        "Change text d[<bl=ideographic,f=ff0000>, <baseline>] and use different "
        "d[<w=w100,f=00ff00>, <font>] d[<w=w900,f=0000ff>, <weights>]."
    )

    page.add(
        ft.Text("\nComplex Styling Example", size=24, weight=ft.FontWeight.BOLD),
        ft.SelectionArea(content=DString(complex_demo).to_flet()),
    )

    # Basic Gradient Demo
    basic_gradient = (
        "Basic gradients: "
        "d[<gs=ff0000,ge=0000ff>, <Red to Blue>], "
        "d[<gs=ffff00,ge=800080>, <Yellow to Purple>]"
    )
    page.add(
        ft.Text("Basic Gradients", size=24, weight=ft.FontWeight.BOLD),
        DString(basic_gradient).to_flet(),
    )

    # Gradient with Style Combinations
    styled_gradient = (
        "Styled gradients: "
        "d[<gs=ff0000,ge=00ff00,size=24,b>, <Bold Gradient>], "
        "d[<gs=00ffff,ge=ff00ff,i,u>, <Italic Underlined>]"
    )
    page.add(
        ft.Text("Styled Gradients", size=24, weight=ft.FontWeight.BOLD),
        DString(styled_gradient).to_flet(),
    )

    # Long Text Gradient
    long_gradient = (
        "Long text gradient: "
        "d[<gs=ff0000,ge=0000ff>, <This is a longer piece of text showing smooth color transition across multiple words>]"
    )
    page.add(
        ft.Text("Long Text Gradient", size=24, weight=ft.FontWeight.BOLD),
        DString(long_gradient).to_flet(),
    )

    # Rainbow-like Gradient
    rainbow = (
        "d[<gs=ff0000,ge=ff8000>, <R>]"
        "d[<gs=ff8000,ge=ffff00>, <a>]"
        "d[<gs=ffff00,ge=00ff00>, <i>]"
        "d[<gs=00ff00,ge=0000ff>, <n>]"
        "d[<gs=0000ff,ge=8000ff>, <b>]"
        "d[<gs=8000ff,ge=ff00ff>, <o>]"
        "d[<gs=ff00ff,ge=ff0080>, <w>]"
    )
    page.add(
        ft.Text("Rainbow Effect", size=24, weight=ft.FontWeight.BOLD),
        DString(rainbow).to_flet(),
    )

    page.scroll = ft.ScrollMode.AUTO
    page.update()


if __name__ == "__main__":
    ft.app(target=create_demo_page)
