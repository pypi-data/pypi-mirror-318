from graphene_django.views import GraphQLView


class GraphiQLOfflineView(GraphQLView):
    graphiql_template = "graphene_django_graphiql_static/graphiql_mod.html"
    whatwg_fetch_sri = "sha256-+pQdxwAcHJdQ3e/9S4RK6g8ZkwdMgFQuHvLuN5uyk5c="

    # React and ReactDOM.
    react_sri = "sha256-Ipu/TQ50iCCVZBUsZyNJfxrDk0E2yhaEIz0vqI+kFG8="
    react_dom_sri = "sha256-nbMykgB6tsOFJ7OdVmPpdqMFVk4ZsqWocT6issAPUF0="

    # The GraphiQL React app.
    graphiql_sri = "sha256-xWTeBbldGE4sW6XOryY1gh9r+S8tV3e3TZEAT/a1kdE="
    graphiql_css_sri = "sha256-xs1Lg/AcXh/0l113vJVxhNzm3sAVX7+cxNkZDrqKe50="

    # The websocket transport library for subscriptions.
    subscriptions_transport_ws_sri = (
        "sha256-EZhvg6ANJrBsgLvLAa0uuHNLepLJVCFYS+xlb5U/bqw="
    )

    graphiql_plugin_explorer_sri = "sha256-3hUuhBXdXlfCj6RTeEkJFtEh/kUG+TCDASFpFPLrzvE="
    graphiql_plugin_explorer_css_sri = (
        "sha256-fA0LPUlukMNR6L4SPSeFqDTYav8QdWjQ2nr559Zln1U="
    )
