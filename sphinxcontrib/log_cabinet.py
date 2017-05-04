from itertools import groupby

from docutils import nodes
from pkg_resources import parse_version
from sphinx.addnodes import versionmodified

__version__ = '1.0.0'


def setup(app):
    app.add_config_value('changelog_collapse_all', False, 'html')
    app.connect('doctree-resolved', handle_doctree_resolved)
    app.add_node(
        CollapsedLog,
        html=(html_visit_CollapsedLog, html_depart_CollapsedLog),
        latex=(visit_nop, visit_nop),
        text=(visit_nop, visit_nop),
        man=(visit_nop, visit_nop),
        texinfo=(visit_nop, visit_nop),
    )

    return {
        'version': __version__,
    }


def handle_doctree_resolved(app, doctree, docname):
    visitor = ChangelogVisitor(doctree, app)
    doctree.walk(visitor)
    collapse_all = app.config.changelog_collapse_all
    version = parse_version(app.config.version)

    for after, log in visitor.logs:
        index = after.parent.index(after) + 1 if after is not None else 0
        del after.parent[index:index + len(log)]

        if not collapse_all:
            visible = []
            hidden = []

            for n in log:
                if (
                    parse_version(n['version']) >= version
                    or n['type'] == 'deprecated'
                ):
                    visible.append(n)
                else:
                    hidden.append(n)

            if visible:
                after.parent.insert(index, visible)
                index += len(visible)
                log = hidden

        collapsed = CollapsedLog()
        collapsed.extend(log)
        after.parent.insert(index, collapsed)


class ChangelogVisitor(nodes.GenericNodeVisitor):
    def __init__(self, document, app):
        super(ChangelogVisitor, self).__init__(document)
        self.logs = []

    def default_visit(self, node):
        after = None

        for key, group in groupby(
            node.children,
            key=lambda n: isinstance(n, versionmodified)
        ):
            if not key:
                after = list(group)[-1]
                continue

            self.logs.append((after, sorted(
                group,
                key=lambda n: parse_version(n['version']),
                reverse=True
            )))

    def default_departure(self, node):
        pass

    unknown_visit = default_visit
    unknown_departure = default_departure


class CollapsedLog(nodes.General, nodes.Element):
    pass


def html_visit_CollapsedLog(self, node):
    self.body.append(self.starttag(node, 'details', CLASS='changelog'))
    self.body.append('<summary>Changelog</summary>')


def html_depart_CollapsedLog(self, node):
    self.body.append('</details>')


def visit_nop(self, node):
    pass
