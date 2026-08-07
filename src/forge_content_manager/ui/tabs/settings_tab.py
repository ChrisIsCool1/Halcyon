"""Settings tab implementation."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import replace
from pathlib import Path
from tkinter import filedialog

import customtkinter as ctk

from forge_content_manager.constants import APPEARANCE_MODES
from forge_content_manager.models import AppSettings, ForgePaths
from forge_content_manager.services.settings_service import SettingsService
from forge_content_manager.ui.dialogs import CardsFolderHelpDialog
from forge_content_manager.ui.widgets import LabeledValue


class SettingsTab(ctk.CTkFrame):
    """Display paths, theme controls, and application settings in a scrollable view."""

    def __init__(
        self,
        master: ctk.CTkBaseClass,
        settings_service: SettingsService,
        current_settings: AppSettings,
        on_appearance_changed: Callable[[str], None],
        on_forge_paths_changed: Callable[[ForgePaths], bool],
        on_reference_cards_changed: Callable[[Path | None], None],
        on_documentation_pack_imported: Callable[[Path], bool],
        on_documentation_pack_reset: Callable[[], None],
    ) -> None:
        """Build the settings view and wire the appearance mode selector."""
        super().__init__(master)
        self._settings_service = settings_service
        self._settings = current_settings
        self._on_appearance_changed = on_appearance_changed
        self._on_forge_paths_changed = on_forge_paths_changed
        self._on_reference_cards_changed = on_reference_cards_changed
        self._on_documentation_pack_imported = on_documentation_pack_imported
        self._on_documentation_pack_reset = on_documentation_pack_reset

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        scrollable_frame = ctk.CTkScrollableFrame(self, label_text="Settings")
        scrollable_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=(16, 8), pady=16)
        scrollable_frame.grid_columnconfigure(0, weight=1)
        scrollable_frame.grid_columnconfigure(1, weight=1)
        scrollable_frame.grid_rowconfigure(2, weight=1)
        appearance_frame = ctk.CTkFrame(scrollable_frame)
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

        path_frame = ctk.CTkFrame(scrollable_frame)
        path_frame.grid(row=0, column=1, sticky="nsew", padx=(8, 16), pady=16)
        path_frame.grid_columnconfigure(0, weight=1)
        path_frame.grid_columnconfigure(1, weight=0)

        path_title = ctk.CTkLabel(path_frame, text="Forge Paths", font=ctk.CTkFont(size=20, weight="bold"))
        path_title.grid(row=0, column=0, sticky="w", padx=16, pady=(16, 8))

        self._path_widgets: dict[str, LabeledValue] = {}
        values = [
            ("custom_cards_dir", "Custom Cards"),
            ("custom_tokens_dir", "Custom Tokens"),
            ("custom_editions_dir", "Custom Editions"),
            ("custom_starter_decks_dir", "Starter Decks"),
            ("card_images_dir", "Card Images"),
            ("token_images_dir", "Token Images"),
            ("backups_dir", "Backups"),
            ("logs_dir", "Logs"),
        ]
        for row, (field_name, label) in enumerate(values, start=1):
            widget = LabeledValue(path_frame, label=label, value=str(getattr(settings_service.paths, field_name)))
            widget.grid(row=row, column=0, sticky="ew", padx=16, pady=8)
            self._path_widgets[field_name] = widget
            ctk.CTkButton(
                path_frame,
                text="Choose",
                width=90,
                command=lambda name=field_name: self._choose_forge_path(name),
            ).grid(row=row, column=1, sticky="e", padx=(0, 16), pady=8)

        settings_file = LabeledValue(path_frame, label="Settings File", value=str(settings_service.paths.settings_file))
        settings_file.grid(row=len(values) + 1, column=0, columnspan=2, sticky="ew", padx=16, pady=8)

        reference_frame = ctk.CTkFrame(scrollable_frame)
        reference_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=16, pady=(0, 16))
        reference_frame.grid_columnconfigure(0, weight=1)
        reference_frame.grid_columnconfigure(1, weight=1)
        reference_title = ctk.CTkFrame(reference_frame, fg_color="transparent")
        reference_title.grid(row=0, column=0, columnspan=2, sticky="w", padx=16, pady=(16, 4))
        ctk.CTkLabel(reference_title, text="Script Editor Reference Cards", font=ctk.CTkFont(size=20, weight="bold")).pack(side="left")
        ctk.CTkButton(
            reference_title,
            text="?",
            width=28,
            height=28,
            command=self._show_reference_cards_help,
        ).pack(side="left", padx=(10, 0))
        self._reference_label = ctk.CTkLabel(reference_frame, text=self._reference_text(), anchor="w", justify="left", wraplength=720)
        self._reference_label.grid(row=1, column=0, sticky="ew", padx=16, pady=(0, 10))
        ctk.CTkButton(reference_frame, text="Choose cardsfolder", command=self._choose_reference_cards).grid(row=1, column=1, sticky="e", padx=16, pady=(0, 10))

        documentation_frame = ctk.CTkFrame(scrollable_frame)
        documentation_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=16, pady=(0, 16))
        documentation_frame.grid_columnconfigure(0, weight=1)
        documentation_frame.grid_columnconfigure(1, weight=1)
        ctk.CTkLabel(documentation_frame, text="Script Documentation Pack", font=ctk.CTkFont(size=20, weight="bold")).grid(row=0, column=0, sticky="w", padx=16, pady=(16, 4))
        self._documentation_label = ctk.CTkLabel(documentation_frame, text=self._documentation_text(), anchor="w", justify="left", wraplength=620)
        self._documentation_label.grid(row=1, column=0, sticky="ew", padx=16, pady=(0, 10))
        controls = ctk.CTkFrame(documentation_frame, fg_color="transparent")
        controls.grid(row=1, column=1, sticky="e", padx=16, pady=(0, 10))
        ctk.CTkButton(controls, text="Import pack", command=self._import_documentation_pack).pack(side="right")
        ctk.CTkButton(controls, text="Use bundled", command=self._reset_documentation_pack).pack(side="right", padx=(8, 0))

    def _change_appearance(self, appearance_mode: str) -> None:
        """Apply the selected appearance mode and persist it."""
        self._settings.appearance_mode = appearance_mode  # type: ignore[assignment]
        self._settings_service.save(self._settings)
        self._on_appearance_changed(appearance_mode)

    def _choose_forge_path(self, field_name: str) -> None:
        """Choose and apply one of the configurable Forge folders."""
        current_path = getattr(self._settings_service.paths, field_name)
        initial_dir = current_path if current_path.is_dir() else current_path.parent if current_path.parent.is_dir() else None
        display_name = field_name.removesuffix("_dir").replace("_", " ").title()
        dialog_options = {"title": f"Choose {display_name} Folder"}
        if initial_dir is not None:
            dialog_options["initialdir"] = str(initial_dir)
        directory = filedialog.askdirectory(**dialog_options)
        if not directory:
            return
        new_settings = replace(self._settings, **{field_name: Path(directory)})
        new_paths = self._settings_service.resolve_paths(new_settings)
        if not self._on_forge_paths_changed(new_paths):
            return
        self._settings = new_settings
        self._settings_service.save(self._settings)
        self._path_widgets[field_name].set_value(str(getattr(new_paths, field_name)))

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

    def _show_reference_cards_help(self) -> None:
        """Open the walkthrough for finding and importing Forge's cardsfolder."""
        CardsFolderHelpDialog(self.winfo_toplevel())

    def _reference_text(self) -> str:
        if self._settings.reference_cards_dir is None:
            return "No optional cardsfolder configured. Packaged builds still include keyword documentation."
        return f"Reference cards folder: {self._settings.reference_cards_dir}\nA background SQLite index is rebuilt after you choose a folder."

    def _import_documentation_pack(self) -> None:
        filename = filedialog.askopenfilename(title="Import Script Documentation Pack", filetypes=[("Documentation Packs", "*.sqlite3 *.db"), ("All Files", "*.*")])
        if filename and self._on_documentation_pack_imported(Path(filename)):
            self._documentation_label.configure(text=self._documentation_text())

    def _reset_documentation_pack(self) -> None:
        self._on_documentation_pack_reset()
        self._documentation_label.configure(text=self._documentation_text())

    def _documentation_text(self) -> str:
        if self._settings.documentation_pack_source is None:
            return "Using the documentation pack bundled with this application."
        return f"Using imported documentation pack:\n{self._settings.documentation_pack_source}"
