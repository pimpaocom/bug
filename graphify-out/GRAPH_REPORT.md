# Graph Report - /root/.claude  (2026-04-28)

## Corpus Check
- Corpus is ~8,020 words - fits in a single context window. You may not need a graph.

## Summary
- 31 nodes · 37 edges · 7 communities detected
- Extraction: 78% EXTRACTED · 22% INFERRED · 0% AMBIGUOUS · INFERRED: 8 edges (avg confidence: 0.82)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Graphify Core Pipeline|Graphify Core Pipeline]]
- [[_COMMUNITY_Session Start Hook|Session Start Hook]]
- [[_COMMUNITY_Graph Analysis|Graph Analysis]]
- [[_COMMUNITY_Extraction Engine|Extraction Engine]]
- [[_COMMUNITY_Continuous Sync|Continuous Sync]]
- [[_COMMUNITY_Audit & Reporting|Audit & Reporting]]
- [[_COMMUNITY_Graph Storage|Graph Storage]]

## God Nodes (most connected - your core abstractions)
1. `Graphify` - 21 edges
2. `Session Start Hook Skill` - 5 edges
3. `Session Start Hook Script` - 4 edges
4. `Community Detection` - 3 edges
5. `Semantic Extraction` - 3 edges
6. `Watch Mode` - 3 edges
7. `Knowledge Graph` - 2 edges
8. `GRAPH_REPORT.md` - 2 edges
9. `graph.json` - 2 edges
10. `AST Structural Extraction` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Graphify Skill` --references--> `Graphify`  [EXTRACTED]
  .claude/CLAUDE.md → .claude/skills/graphify/SKILL.md

## Hyperedges (group relationships)
- **Graphify Output Pipeline** — graphify_knowledge_graph, graphify_html_viz, graphify_graph_report, graphify_graph_json [EXTRACTED 0.95]
- **Graphify Extraction Pipeline** — graphify_detect, graphify_ast_extraction, graphify_semantic_extraction, graphify_subagent [EXTRACTED 0.90]
- **Session Start Hook Setup Workflow** — session_start_hook_script, session_start_settings_json, session_start_dependency_install [EXTRACTED 0.95]

## Communities

### Community 0 - "Graphify Core Pipeline"
Cohesion: 0.17
Nodes (12): Graphify Skill, Graph Build (graphify.build), Graph Cluster (graphify.cluster), File Detection (graphify.detect), Graph Export (graphify.export), Interactive HTML Visualization, MCP Server, Neo4j Export (+4 more)

### Community 1 - "Session Start Hook"
Cohesion: 0.53
Nodes (6): Async Hook Mode, Dependency Installation, Hook Environment Variables, Session Start Hook Script, Claude Settings JSON, Session Start Hook Skill

### Community 2 - "Graph Analysis"
Cohesion: 0.67
Nodes (3): Community Detection, God Nodes, Surprising Connections

### Community 3 - "Extraction Engine"
Cohesion: 0.67
Nodes (3): AST Structural Extraction, Semantic Extraction, Graphify Extraction Subagent

### Community 4 - "Continuous Sync"
Cohesion: 0.67
Nodes (3): Git Post-Commit Hook, Incremental Update (--update), Watch Mode

### Community 5 - "Audit & Reporting"
Cohesion: 1.0
Nodes (2): Audit Trail, GRAPH_REPORT.md

### Community 6 - "Graph Storage"
Cohesion: 1.0
Nodes (2): graph.json, Knowledge Graph

## Knowledge Gaps
- **15 isolated node(s):** `Graphify Skill`, `Interactive HTML Visualization`, `Obsidian Vault Export`, `Neo4j Export`, `MCP Server` (+10 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Audit & Reporting`** (2 nodes): `Audit Trail`, `GRAPH_REPORT.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Graph Storage`** (2 nodes): `graph.json`, `Knowledge Graph`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Graphify` connect `Graphify Core Pipeline` to `Graph Analysis`, `Extraction Engine`, `Continuous Sync`, `Audit & Reporting`, `Graph Storage`?**
  _High betweenness centrality (0.610) - this node is a cross-community bridge._
- **Why does `Community Detection` connect `Graph Analysis` to `Graphify Core Pipeline`?**
  _High betweenness centrality (0.103) - this node is a cross-community bridge._
- **Why does `Semantic Extraction` connect `Extraction Engine` to `Graphify Core Pipeline`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Session Start Hook Script` (e.g. with `Async Hook Mode` and `Dependency Installation`) actually correct?**
  _`Session Start Hook Script` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Community Detection` (e.g. with `God Nodes` and `Surprising Connections`) actually correct?**
  _`Community Detection` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Graphify Skill`, `Interactive HTML Visualization`, `Obsidian Vault Export` to the rest of the system?**
  _15 weakly-connected nodes found - possible documentation gaps or missing edges._