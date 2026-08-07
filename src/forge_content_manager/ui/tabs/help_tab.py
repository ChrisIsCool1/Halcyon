"""Bundled help wiki tab."""

from __future__ import annotations

import re
import tkinter as tk

import customtkinter as ctk

from forge_content_manager.services.help_wiki_service import HelpGroup, HelpPage


class HelpTab(ctk.CTkFrame):
    """Searchable, read-only help wiki with collapsible page groups."""

    def __init__(self, master: ctk.CTkBaseClass, groups: tuple[HelpGroup, ...]) -> None:
        super().__init__(master)
        self._groups = groups
        self._group_expanded = {group.group_id: True for group in groups}
        self._group_buttons: dict[str, ctk.CTkButton] = {}
        self._page_buttons: dict[str, ctk.CTkButton] = {}
        self._pages_by_slug = {page.slug: page for group in groups for page in group.pages}
        self._selected_slug: str | None = None

        self.grid_columnconfigure(0, weight=0, minsize=290)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        navigation = ctk.CTkFrame(self, corner_radius=0)
        navigation.grid(row=0, column=0, sticky="nsew", padx=(16, 8), pady=16)
        navigation.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(navigation, text="Help Wiki", font=ctk.CTkFont(size=22, weight="bold")).grid(
            row=0, column=0, sticky="w", padx=16, pady=(16, 4)
        )
        ctk.CTkLabel(
            navigation,
            text="Search the guides or expand a group to browse related pages.",
            justify="left",
            wraplength=250,
        ).grid(row=1, column=0, sticky="w", padx=16, pady=(0, 12))

        search_frame = ctk.CTkFrame(navigation, fg_color="transparent")
        search_frame.grid(row=2, column=0, sticky="new", padx=12, pady=(0, 8))
        search_frame.grid_columnconfigure(0, weight=1)
        self._search = ctk.CTkEntry(search_frame, placeholder_text="Search help pages")
        self._search.grid(row=0, column=0, sticky="ew")
        self._search.bind("<KeyRelease>", self._handle_search)
        ctk.CTkButton(search_frame, text="Clear", width=58, command=self._clear_search).grid(row=0, column=1, padx=(6, 0))

        self._navigation_scroll = ctk.CTkScrollableFrame(navigation, fg_color="transparent")
        self._navigation_scroll.grid(row=3, column=0, sticky="nsew", padx=8, pady=(0, 8))
        self._navigation_scroll.grid_columnconfigure(0, weight=1)
        navigation.grid_rowconfigure(3, weight=1)

        content = ctk.CTkFrame(self)
        content.grid(row=0, column=1, sticky="nsew", padx=(8, 16), pady=16)
        content.grid_columnconfigure(0, weight=1)
        content.grid_rowconfigure(1, weight=1)
        self._page_title = ctk.CTkLabel(content, text="Select a help page", anchor="w", font=ctk.CTkFont(size=24, weight="bold"))
        self._page_title.grid(row=0, column=0, sticky="ew", padx=24, pady=(24, 4))
        self._page_view = tk.Text(
            content,
            wrap="word",
            padx=24,
            pady=18,
            relief="flat",
            borderwidth=0,
            font=("Segoe UI", 11),
            state="disabled",
        )
        self._page_view.grid(row=1, column=0, sticky="nsew", padx=8, pady=(0, 8))
        scrollbar = ctk.CTkScrollbar(content, command=self._page_view.yview)
        scrollbar.grid(row=1, column=1, sticky="ns", pady=(0, 8), padx=(0, 8))
        self._page_view.configure(yscrollcommand=scrollbar.set)
        self._configure_text_tags()

        self._rebuild_navigation()
        first_page = next(iter(self._pages_by_slug.values()), None)
        if first_page:
            self._select_page(first_page)
        else:
            self._show_empty_state()

    def _configure_text_tags(self) -> None:
        self._page_view.tag_configure("heading", font=("Segoe UI", 18, "bold"), spacing1=14, spacing3=6)
        self._page_view.tag_configure("subheading", font=("Segoe UI", 13, "bold"), spacing1=10, spacing3=4)
        self._page_view.tag_configure("body", spacing3=8)
        self._page_view.tag_configure("bullet", lmargin1=18, lmargin2=34, spacing3=5)
        self._page_view.tag_configure("code", font=("Cascadia Mono", 10), lmargin1=18, lmargin2=18, spacing1=5, spacing3=5)

    def _rebuild_navigation(self, matches: dict[str, tuple[HelpPage, ...]] | None = None) -> None:
        for widget in self._navigation_scroll.winfo_children():
            widget.destroy()
        self._group_buttons.clear()
        self._page_buttons.clear()
        for group in self._groups:
            pages = matches[group.group_id] if matches is not None else group.pages
            if not pages:
                continue
            button = ctk.CTkButton(
                self._navigation_scroll,
                text=self._group_label(group),
                anchor="w",
                fg_color="transparent",
                text_color=("#000000", "#ffffff"),
                command=lambda group_id=group.group_id: self._toggle_group(group_id),
            )
            button.pack(fill="x", pady=(4, 0))
            self._group_buttons[group.group_id] = button
            if matches is not None or self._group_expanded.get(group.group_id, True):
                for page in pages:
                    page_button = ctk.CTkButton(
                        self._navigation_scroll,
                        text=page.title,
                        anchor="w",
                        fg_color="transparent",
                        text_color=("#000000", "#ffffff"),
                        hover_color=("#dce8fb", "#7594c5"),
                        command=lambda selected=page: self._select_page(selected),
                    )
                    page_button.pack(fill="x", padx=(14, 0), pady=1)
                    self._page_buttons[page.slug] = page_button
        self._highlight_selected_page()

    def _group_label(self, group: HelpGroup) -> str:
        return f"{'▾' if self._group_expanded.get(group.group_id, True) else '▸'}  {group.title}"

    def _toggle_group(self, group_id: str) -> None:
        self._group_expanded[group_id] = not self._group_expanded.get(group_id, True)
        self._rebuild_navigation()

    def _handle_search(self, _event=None) -> None:
        query = self._search.get().strip().casefold()
        if not query:
            self._rebuild_navigation()
            return
        terms = [term for term in re.split(r"\s+", query) if term]
        matches = {
            group.group_id: tuple(page for page in group.pages if all(term in page.search_text for term in terms))
            for group in self._groups
        }
        self._rebuild_navigation(matches)

    def _clear_search(self) -> None:
        self._search.delete(0, "end")
        self._handle_search()
        self._search.focus_set()

    def _select_page(self, page: HelpPage) -> None:
        self._selected_slug = page.slug
        self._page_title.configure(text=page.title)
        self._page_view.configure(state="normal")
        self._page_view.delete("1.0", "end")
        self._render_markdown(page.content)
        self._page_view.configure(state="disabled")
        self._page_view.yview_moveto(0)
        self._highlight_selected_page()

    def _show_empty_state(self) -> None:
        self._page_title.configure(text="Help is unavailable")
        self._page_view.configure(state="normal")
        self._page_view.insert("1.0", "No bundled help pages were found.")
        self._page_view.configure(state="disabled")

    def _highlight_selected_page(self) -> None:
        for slug, button in self._page_buttons.items():
            button.configure(fg_color=("#c8dcfb", "#7594c5") if slug == self._selected_slug else "transparent")

    def _render_markdown(self, content: str) -> None:
        in_code = False
        for raw_line in content.splitlines():
            line = raw_line.rstrip()
            if line.startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                self._page_view.insert("end", f"{line}\n", "code")
            elif line.startswith("# "):
                self._page_view.insert("end", f"{line[2:]}\n", "heading")
            elif line.startswith("## "):
                self._page_view.insert("end", f"{line[3:]}\n", "subheading")
            elif line.startswith(("- ", "* ")):
                self._page_view.insert("end", f"• {line[2:]}\n", "bullet")
            elif line:
                self._page_view.insert("end", f"{line}\n", "body")
            else:
                self._page_view.insert("end", "\n", "body")
