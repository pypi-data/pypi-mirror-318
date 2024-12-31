import base64
import json
import logging
from typing import Any
from uuid import uuid4

import dash_mantine_components as dmc
from dash import (
    ALL,
    MATCH,
    Dash,
    Input,
    Output,
    State,
    ctx,
    dcc,
    html,
    no_update,
    _dash_renderer,
)
from dash_snap_grid import ResponsiveGrid

from . import utils
from .card_manager import CardManager

_dash_renderer._set_react_version("18.2.0")


class CardCanvas:
    def __init__(self, settings: dict[str, Any]):
        self.settings = settings
        self.card_manager = CardManager()

    def run(self):
        self.app.run_server(debug=True)

    @property
    def app(self):
        if not hasattr(self, "_app"):
            self._app = self._create_app(self.settings)
        return self._app

    def _create_app(self, settings: dict[str, Any]) -> Dash:
        title = settings.get("title", "Dash Dash")
        start_config = settings.get("start_config", {})
        logo = settings.get("logo", None)
        app = Dash(__name__)
        app.title = title
        app.config.suppress_callback_exceptions = True

        title_layout = utils.get_title_layout(title, logo)

        main_buttons = dmc.Group(
            [
                utils.render_buttons(
                    [
                        {
                            "id": "open-settings",
                            "label": "Open Settings",
                            "icon": "mdi:settings",
                        },
                        {"id": "add-cards", "label": "Add Cards", "icon": "mdi:plus"},
                        {
                            "id": "",
                            "label": "Layout",
                            "children": [
                                {
                                    "id": "upload-layout",
                                    "type": "upload",
                                    "label": "Upload Layout",
                                    "icon": "mdi:upload",
                                },
                                {
                                    "id": "download-layout",
                                    "label": "Download Layout",
                                    "icon": "mdi:download",
                                },
                                {
                                    "id": "save-layout",
                                    "label": "Save Layout",
                                    "icon": "mdi:content-save",
                                },
                                {
                                    "id": "reset-layout",
                                    "label": "Reset Layout",
                                    "icon": "mdi:refresh",
                                    "options": {"bg": "#ffcccc", "color": "darkgrey"},
                                },
                            ],
                        },
                    ]
                ),
                dmc.Checkbox(
                    "Editable Layout",
                    id="edit-layout",
                    size="xs",
                    checked=False,
                    persistence=True,
                ),
            ],
            m="xs",
            mt=0,
        )

        stage_layout = dmc.Container(
            fluid=True,
            children=[
                title_layout,
                main_buttons,
                ResponsiveGrid(
                    id="card-grid",
                    cols={"lg": 18, "md": 12, "sm": 6, "xs": 4, "xxs": 2},
                    rowHeight=50,
                    # compactType="vertical",
                    draggableCancel=".no-drag *",
                    isDroppable=True,
                    layouts={"lg": []},
                    width=100,
                ),
            ],
        )

        invisible_controls = html.Div(
            [
                dcc.Store(id="main-store", storage_type="local"),
                dcc.Store(id="card-config-store", storage_type="memory"),
                dcc.Store(id="card-layout-store", storage_type="memory"),
                dcc.Download(id="download-layout-data"),
            ]
        )

        settings_layout = dmc.Drawer(
            id="settings-layout",
            padding="md",
            closeOnClickOutside=False,
            withOverlay=False,
        )

        app.layout = dmc.MantineProvider(
            [stage_layout, settings_layout, invisible_controls]
        )

        @app.callback(
            Output("card-layout-store", "data"),
            Output("card-config-store", "data"),
            Input(app.layout, "layout"),
            State("main-store", "data"),
        )
        def initial_load(_app_layout, main_store):
            if main_store and isinstance(main_store, dict):
                card_layouts = main_store.get("card_layouts", {"lg": []})
                card_config = main_store.get("card_config", start_config)
                return card_layouts, card_config
            return {"lg": []}, start_config

        @app.callback(
            Output("card-grid", "children"),
            Output("card-grid", "layouts"),
            Input("card-config-store", "data"),
            State("card-layout-store", "data"),
        )
        def load_cards(card_config, card_layouts):
            return self.card_manager.render(card_config, {}), card_layouts

        @app.callback(
            Output("main-store", "data"),
            Output("card-layout-store", "data", allow_duplicate=True),
            Input("save-layout", "n_clicks"),
            State("card-grid", "layouts"),
            State("card-config-store", "data"),
            prevent_initial_call=True,
        )
        def save_reset_cards(nclicks, card_layouts, card_config):
            if not nclicks:
                return no_update
            return {
                "card_layouts": card_layouts,
                "card_config": card_config,
            }, card_layouts

        @app.callback(
            Output("card-layout-store", "data", allow_duplicate=True),
            Output("card-config-store", "data", allow_duplicate=True),
            Input("reset-layout", "n_clicks"),
            State("main-store", "data"),
            prevent_initial_call=True,
        )
        def reset_layouts(nclicks, main_store):
            if not nclicks or not main_store or not isinstance(main_store, dict):
                return no_update, no_update
            return main_store.get("card_layouts", {"lg": []}), main_store.get(
                "card_config", start_config
            )

        @app.callback(
            Output("settings-layout", "opened"),
            Output("settings-layout", "children"),
            Input("open-settings", "n_clicks"),
            prevent_initial_call=True,
        )
        def open_settings(nclicks):
            children = [
                dmc.Stack(
                    [
                        dmc.Title("Settings", order=2),
                        dmc.Text(
                            "These are the global settings. These apply to all the cards",
                            variant="muted",
                        ),
                    ]
                )
            ]
            return True, children

        @app.callback(
            Output("settings-layout", "opened", allow_duplicate=True),
            Output("settings-layout", "children", allow_duplicate=True),
            Input("add-cards", "n_clicks"),
            prevent_initial_call=True,
        )
        def add_cards(nclicks):
            children = [
                dmc.Stack(
                    [
                        dmc.Title("Add Cards", order=2),
                        dmc.Text(
                            "These are the cards you can add to the dashboard."
                            " Drag and drop them on the grid where you want them to be",
                            variant="muted",
                        ),
                        dmc.Stack(
                            [
                                utils.render_card_preview(card_class)
                                for card_class in self.card_manager.card_classes.values()
                            ]
                        ),
                    ]
                )
            ]
            return True, children

        @app.callback(
            Output("card-config-store", "data", allow_duplicate=True),
            Output("card-layout-store", "data", allow_duplicate=True),
            Input("card-grid", "droppedItem"),
            State("card-config-store", "data"),
            State("card-layout-store", "data"),
            prevent_initial_call=True,
        )
        def add_new_card(dropped_item, card_config, card_layouts):
            if not dropped_item:
                return no_update, no_update
            card_id = str(uuid4())
            card_config[card_id] = {"card_class": dropped_item["i"], "settings": {}}
            new_layout_item = {
                "i": card_id,
                "x": dropped_item["x"],
                "y": dropped_item["y"],
                "w": dropped_item["w"],
                "h": dropped_item["h"],
            }
            if not card_layouts:
                card_layouts = {"lg": []}
            for key in card_layouts.keys():
                card_layouts[key].append(new_layout_item)
            return card_config, card_layouts

        @app.callback(
            Output("card-config-store", "data", allow_duplicate=True),
            Input({"type": "card-delete", "index": ALL}, "n_clicks"),
            State("card-config-store", "data"),
            prevent_initial_call=True,
        )
        def delete_card(nclicks, card_config):
            if not card_config:
                return no_update
            if not any(nclicks) or not ctx.triggered:
                return no_update
            if not ctx.triggered_id or not isinstance(ctx.triggered_id, dict):
                return no_update
            card_id = ctx.triggered_id.get("index")
            card_config.pop(card_id, None)
            return card_config

        @app.callback(
            Output("settings-layout", "children", allow_duplicate=True),
            Output("settings-layout", "opened", allow_duplicate=True),
            Input({"type": "card-settings", "index": ALL}, "n_clicks"),
            State("card-config-store", "data"),
            prevent_initial_call=True,
        )
        def open_card_settings(nclicks, card_config):
            if not any(nclicks) or not ctx.triggered or not ctx.triggered_id:
                return no_update, no_update
            if not card_config:
                card_config = start_config
            card_id = ctx.triggered_id.get("index")
            card_objects = self.card_manager.card_objects(
                card_config, {"username": "yyxxxxx"}
            )
            if card_id not in card_objects:
                return dmc.Alert("Card not found", color="red"), True
            card = card_objects[card_id]
            return dmc.Stack(
                [
                    card.render_settings(),
                    dmc.Button(
                        "OK",
                        id="settings_ok",
                    ),
                ]
            ), True

        @app.callback(
            Output("card-config-store", "data", allow_duplicate=True),
            Output("settings-layout", "opened", allow_duplicate=True),
            Input("settings_ok", "n_clicks"),
            State({"type": "card-settings", "id": ALL, "sub-id": ALL}, "value"),
            State({"type": "card-settings", "id": ALL, "sub-id": ALL}, "id"),
            State("card-config-store", "data"),
            prevent_initial_call=True,
        )
        def save_card_settings(nclicks, values, ids, card_config):
            if not nclicks or not ctx.triggered:
                return no_update, no_update
            for idx, val in zip(ids, values):
                card_id = idx.get("id")
                sub_id = idx.get("sub-id")
                if card_id not in card_config:
                    continue
                card_config[card_id]["settings"][sub_id] = val
            return card_config, False

        @app.callback(
            Output("card-grid", "isDraggable"),
            Output("card-grid", "isResizable"),
            Output({"type": "card-menu", "index": ALL}, "style"),
            Input({"type": "card-menu", "index": ALL}, "id"),
            Input("edit-layout", "checked"),
            prevent_initial_call=True,
        )
        def toggle_edit_mode(ids, checked):
            if checked:
                return True, True, [{"display": "block"}] * len(ids)
            return False, False, [{"display": "none"}] * len(ids)

        @app.callback(
            Output({"type": "card-content", "index": MATCH}, "children"),
            Output({"type": "card-interval", "index": MATCH}, "interval"),
            Input({"type": "card-interval", "index": MATCH}, "n_intervals"),
            State({"type": "card-interval", "index": MATCH}, "interval"),
            State("card-config-store", "data"),
        )
        def update_card(n_intervals, interval, cards_config):
            if not ctx.triggered_id or not cards_config:
                return no_update
            card_objects = self.card_manager.card_objects(
                cards_config, {"username": "yyxxxxx"}
            )
            card_id = ctx.triggered_id.get("index")
            card = card_objects[card_id]
            return card.render(), card.interval

        @app.callback(
            Output("download-layout-data", "data"),
            Input("download-layout", "n_clicks"),
            State("main-store", "data"),
            prevent_initial_call=True,
        )
        def download_layout(n_clicks, main_store):
            if not n_clicks or not main_store:
                return no_update
            return dict(
                content=json.dumps(main_store), filename="layout.json", type="json"
            )

        @app.callback(
            Output("main-store", "data", allow_duplicate=True),
            Output("card-config-store", "data", allow_duplicate=True),
            Output("card-layout-store", "data", allow_duplicate=True),
            Input("upload-layout", "contents"),
            prevent_initial_call=True,
        )
        def upload_layout(contents):
            if not contents:
                return no_update
            try:
                content_type, content_string = contents.split(",")
                decoded = base64.b64decode(content_string)
                content = decoded.decode("utf-8")
                print(content)
                data = json.loads(content)
                return (
                    data,
                    data.get("card_config", start_config),
                    data.get("card_layouts", {"lg": []}),
                )
            except Exception as e:
                logging.error(e)
            return {}

        return app
