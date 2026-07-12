"""Settings tab implementation."""

from __future__ import annotations

from pathlib import Path
from tkinter import filedialog

import customtkinter as ctk

from forge_content_manager.constants import APPEARANCE_MODES
from forge_content_manager.models import AppSettings
from forge_content_manager.services.settings_service import SettingsService
from forge_content_manager.ui.widgets import LabeledValue


class SettingsTab(ctk.CTkFrame):
    """Display paths, theme controls, and application settings."""

    def __init__(
        self,
        master: ctk.CTkBaseClass,
        settings_service: SettingsService,
        current_settings: AppSettings,
        on_appearance_changed: callable,
        on_reference_cards_changed: callable,
    ) -> None:
        """Build the settings view and wire the appearance mode selector."""
        super().__init__(master)
        self._settings_service = settings_service
        self._settings = current_settings
        self._on_appearance_changed = on_appearance_changed
        self._on_reference_cards_changed = on_reference_cards_changed

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        appearance_frame = ctk.CTkFrame(self)
        appearance_frame.grid(row=0, column=0, sticky="nsew", padx=(16, 8), pady=16)
        appearance_frame.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(appearance_frame, text="Appearance", font=ctk.CTkFont(size=20, weight="bold"))
        title.grid(row=0, column=0, sticky="w", padx=16, pady=(16, 8))

        description = ctk.CTkLabel(
            appearance_frame,
            text="Switch between system, light, and dark modes. The choice is persisted under the Forge custom folder.",
            justify="left",
            wraplength=420,
        )
        description.grid(row=1, column=0, sticky="w", padx=16, pady=(0, 12))

        self.appearance_menu = ctk.CTkOptionMenu(
            appearance_frame,
            values=list(APPEARANCE_MODES),
            command=self._change_appearance,
            width=180,
        )
        self.appearance_menu.set(self._settings.appearance_mode)
        self.appearance_menu.grid(row=2, column=0, sticky="w", padx=16, pady=(0, 16))

        path_frame = ctk.CTkFrame(self)
        path_frame.grid(row=0, column=1, sticky="nsew", padx=(8, 16), pady=16)
        path_frame.grid_columnconfigure(0, weight=1)

        path_title = ctk.CTkLabel(path_frame, text="Forge Paths", font=ctk.CTkFont(size=20, weight="bold"))
        path_title.grid(row=0, column=0, sticky="w", padx=16, pady=(16, 8))

        paths = settings_service._paths
        values = [
            ("Custom Cards", str(paths.custom_cards_dir)),
            ("Custom Editions", str(paths.custom_editions_dir)),
            ("Starter Decks", str(paths.custom_starter_decks_dir)),
            ("Card Images", str(paths.card_images_dir)),
            ("Backups", str(paths.backups_dir)),
            ("Settings File", str(paths.settings_file)),
        ]
        for row, (label, value) in enumerate(values, start=1):
            widget = LabeledValue(path_frame, label=label, value=value)
            widget.grid(row=row, column=0, sticky="ew", padx=16, pady=8)

        reference_frame = ctk.CTkFrame(self)
        reference_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=16, pady=(0, 16))
        reference_frame.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(reference_frame, text="Script Editor Reference Cards", font=ctk.CTkFont(size=20, weight="bold")).grid(row=0, column=0, sticky="w", padx=16, pady=(16, 4))
        self._reference_label = ctk.CTkLabel(reference_frame, text=self._reference_text(), anchor="w", justify="left", wraplength=720)
        self._reference_label.grid(row=1, column=0, sticky="ew", padx=16, pady=(0, 10))
        ctk.CTkButton(reference_frame, text="Choose cardsfolder", command=self._choose_reference_cards).grid(row=1, column=1, padx=16, pady=(0, 10))

    def _change_appearance(self, appearance_mode: str) -> None:
        """Apply the selected appearance mode and persist it."""
        self._settings.appearance_mode = appearance_mode  # type: ignore[assignment]
        self._settings_service.save(self._settings)
        self._on_appearance_changed(appearance_mode)

    def _choose_reference_cards(self) -> None:
        """Persist an optional Forge cardsfolder used by Script Editor search."""
        directory = filedialog.askdirectory(title="Choose Forge cardsfolder")
        if not directory:
            return
        path = Path(directory)
        self._settings.reference_cards_dir = path
        self._settings_service.save(self._settings)
        self._reference_label.configure(text=self._reference_text())
        self._on_reference_cards_changed(path)

    def _reference_text(self) -> str:
        if self._settings.reference_cards_dir is None:
            return "No optional cardsfolder configured. Packaged builds still include keyword documentation."
        return f"Reference cards folder: {self._settings.reference_cards_dir}"
