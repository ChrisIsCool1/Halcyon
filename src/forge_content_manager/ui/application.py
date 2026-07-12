"""Top-level application window."""

from __future__ import annotations

import logging

import customtkinter as ctk

from forge_content_manager.constants import APP_NAME
from forge_content_manager.services.content_service import ForgeContentService
from forge_content_manager.services.settings_service import SettingsService
from forge_content_manager.services.script_authoring_service import ScriptAuthoringService
from forge_content_manager.ui.tabs.card_browser_tab import CardBrowserTab
from forge_content_manager.ui.tabs.card_import_tab import CardImportTab
from forge_content_manager.ui.tabs.settings_tab import SettingsTab
from forge_content_manager.ui.tabs.set_manager_tab import SetManagerTab
from forge_content_manager.ui.tabs.script_editor_tab import ScriptEditorTab


class ForgeContentManagerApp(ctk.CTk):
    """Main application window for Forge Custom Content Manager."""

    def __init__(self, content_service: ForgeContentService, settings_service: SettingsService) -> None:
        """Initialize the root window, persisted settings, and all tab content."""
        super().__init__()
        self._logger = logging.getLogger(self.__class__.__name__)
        self._content_service = content_service
        self._settings_service = settings_service
        self._settings = settings_service.load()
        reference_database = settings_service._paths.settings_file.parent / "script_reference_cards.sqlite3"
        self._authoring_service = ScriptAuthoringService(self._settings.reference_cards_dir, reference_database)

        self.title(APP_NAME)
        self.geometry("1360x900")
        self.minsize(1180, 760)
        ctk.set_appearance_mode(self._settings.appearance_mode)
        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        header = ctk.CTkFrame(self, corner_radius=0)
        header.grid(row=0, column=0, sticky="ew")
        header.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            header,
            text=APP_NAME,
            font=ctk.CTkFont(size=30, weight="bold"),
        )
        title.grid(row=0, column=0, sticky="w", padx=24, pady=(18, 4))

        subtitle = ctk.CTkLabel(
            header,
            text="Manage Forge custom sets, scripts, images, packages, and backups.",
            font=ctk.CTkFont(size=14),
        )
        subtitle.grid(row=1, column=0, sticky="w", padx=24, pady=(0, 16))

        self.tabview = ctk.CTkTabview(self, segmented_button_selected_hover_color=("#2559b5", "#2559b5"))
        self.tabview.grid(row=1, column=0, sticky="nsew", padx=18, pady=(0, 18))

        for tab_name in ("Sets", "Import", "Cards", "Script Editor", "Settings"):
            self.tabview.add(tab_name)
            self.tabview.tab(tab_name).grid_columnconfigure(0, weight=1)
            self.tabview.tab(tab_name).grid_rowconfigure(0, weight=1)

        self.set_manager_tab = SetManagerTab(
            master=self.tabview.tab("Sets"),
            content_service=self._content_service,
            on_sets_changed=self.refresh_data_views,
        )
        self.set_manager_tab.grid(row=0, column=0, sticky="nsew")

        self.card_import_tab = CardImportTab(
            master=self.tabview.tab("Import"),
            content_service=self._content_service,
            on_import_complete=self._handle_import_complete,
        )
        self.card_import_tab.grid(row=0, column=0, sticky="nsew")

        self.card_browser_tab = CardBrowserTab(
            master=self.tabview.tab("Cards"),
            content_service=self._content_service,
            on_cards_changed=self.refresh_data_views,
        )
        self.card_browser_tab.grid(row=0, column=0, sticky="nsew")

        self.script_editor_tab = ScriptEditorTab(
            master=self.tabview.tab("Script Editor"),
            content_service=self._content_service,
            authoring_service=self._authoring_service,
            on_import_complete=self._handle_import_complete,
        )
        self.script_editor_tab.grid(row=0, column=0, sticky="nsew")

        self.settings_tab = SettingsTab(
            master=self.tabview.tab("Settings"),
            settings_service=self._settings_service,
            current_settings=self._settings,
            on_appearance_changed=self._handle_appearance_mode_change,
            on_reference_cards_changed=self._handle_reference_cards_changed,
        )
        self.settings_tab.grid(row=0, column=0, sticky="nsew")

        self.refresh_data_views()

    def refresh_data_views(self) -> None:
        """Refresh all data-driven tabs after content has changed."""
        self.set_manager_tab.refresh()
        self.card_import_tab.refresh_sets()
        self.card_browser_tab.refresh()
        self.script_editor_tab.refresh_sets()

    def _handle_import_complete(self) -> None:
        """Refresh dependent views after a successful import workflow."""
        self.refresh_data_views()
        self.tabview.set("Cards")

    def _handle_appearance_mode_change(self, appearance_mode: str) -> None:
        """Apply and persist a new appearance mode selection."""
        self._settings.appearance_mode = appearance_mode  # type: ignore[assignment]
        self._settings_service.save(self._settings)
        ctk.set_appearance_mode(appearance_mode)
        self._logger.info("Appearance mode changed to %s", appearance_mode)

    def _handle_reference_cards_changed(self, directory) -> None:
        """Apply the optional Script Editor reference-card location."""
        self._authoring_service.set_reference_cards_dir(directory)
        self.script_editor_tab.refresh_reference_cards()

