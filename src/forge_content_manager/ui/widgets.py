"""Reusable customtkinter widgets for the Forge content manager UI."""

from __future__ import annotations

from pathlib import Path
from tkinter import filedialog

import customtkinter as ctk

from forge_content_manager.constants import RARITY_LABELS
from forge_content_manager.models import CardImportInput


class LabeledValue(ctk.CTkFrame):
    """Compact read-only value display used in settings and overview panels."""

    def __init__(self, master: ctk.CTkBaseClass, label: str, value: str) -> None:
        """Create a two-line value display."""
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        caption = ctk.CTkLabel(self, text=label, font=ctk.CTkFont(size=12, weight="bold"))
        caption.grid(row=0, column=0, sticky="w", padx=12, pady=(10, 2))
        self._value_label = ctk.CTkLabel(self, text=value, justify="left", wraplength=240)
        self._value_label.grid(row=1, column=0, sticky="w", padx=12, pady=(0, 10))

    def set_value(self, value: str) -> None:
        """Update the displayed value text."""
        self._value_label.configure(text=value)


class CardImportEntryFrame(ctk.CTkFrame):
    """UI block for entering a single card script, image, and rarity."""

    def __init__(self, master: ctk.CTkBaseClass, index: int, on_remove: callable) -> None:
        """Build the input controls used for one card import row."""
        super().__init__(master)
        self._on_remove = on_remove
        self._image_path: Path | None = None
        self.grid_columnconfigure(0, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=12, pady=(10, 8))
        header.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(header, text=f"Card {index}", font=ctk.CTkFont(size=16, weight="bold"))
        title.grid(row=0, column=0, sticky="w")

        remove_button = ctk.CTkButton(header, text="Remove", command=self._handle_remove, width=90)
        remove_button.grid(row=0, column=1, sticky="e")

        self.script_textbox = ctk.CTkTextbox(self, height=220)
        self.script_textbox.grid(row=1, column=0, sticky="nsew", padx=12, pady=8)

        footer = ctk.CTkFrame(self, fg_color="transparent")
        footer.grid(row=2, column=0, sticky="ew", padx=12, pady=(4, 12))
        footer.grid_columnconfigure(1, weight=1)

        rarity_label = ctk.CTkLabel(footer, text="Rarity")
        rarity_label.grid(row=0, column=0, sticky="w", padx=(0, 12))

        self.rarity_menu = ctk.CTkOptionMenu(footer, values=list(RARITY_LABELS))
        self.rarity_menu.set("Common")
        self.rarity_menu.grid(row=0, column=1, sticky="w")

        image_button = ctk.CTkButton(footer, text="Choose Image", command=self._pick_image, width=140)
        image_button.grid(row=0, column=2, sticky="e", padx=(12, 12))

        self.image_label = ctk.CTkLabel(footer, text="No image selected", width=320, anchor="w")
        self.image_label.grid(row=0, column=3, sticky="ew")

    def get_value(self) -> CardImportInput:
        """Return the current card import input captured by the frame."""
        script_text = self.script_textbox.get("1.0", "end").rstrip()
        return CardImportInput(script_text=script_text, image_source=self._image_path, rarity=self.rarity_menu.get())

    def _pick_image(self) -> None:
        """Open a file dialog for choosing an image source."""
        file_name = filedialog.askopenfilename(
            title="Choose Card Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.webp;*.bmp")],
        )
        if not file_name:
            return
        self._image_path = Path(file_name)
        self.image_label.configure(text=self._image_path.name)

    def _handle_remove(self) -> None:
        """Invoke the owning tab's removal callback."""
        self._on_remove(self)
