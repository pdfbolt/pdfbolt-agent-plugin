# PDFBolt

Generate PDFs from HTML, web pages, or published PDFBolt templates. The plugin also helps you create reusable templates, preview changes, and manage drafts and published versions.

Version 1.0.0 includes Claude and OpenAI manifests, two shared skills, and one remote MCP server. OpenAI end-to-end compatibility has not yet been verified.

The plugin files are available under the [MIT License](LICENSE). This license does not cover the PDFBolt backend or grant access to the hosted service. PDFBolt account requirements, service terms, and conversion-credit limits still apply.

## Connect your account

You need a PDFBolt account. New Free accounts include starter conversion credits, and MCP access is available on the Free plan. Rendering PDFs, previews, and comparisons uses conversion credits; listing templates, checking usage, and validating content does not.

The plugin connects to `https://api.pdfbolt.com/mcp` through OAuth. No API key belongs in the plugin files or in chat. In Claude chat or Cowork, open the installed plugin's Connectors tab, add or connect PDFBolt, and complete the sign-in flow. Installing the plugin alone does not authorize access to your account.

## Try it locally in Claude Code

From the parent directory:

```sh
claude plugin validate ./pdfbolt-agent-plugin
claude --plugin-dir ./pdfbolt-agent-plugin
```

Use `/mcp` to check the connection and complete OAuth when prompted. Test in a clean session without another plugin named `pdfbolt`, to avoid confusing the public package with an internal development plugin.

Example requests:

- “Use PDFBolt to generate a one-page PDF titled Project proposal, with sections for scope, schedule, and next steps. Use placeholders for details I haven't supplied.”
- “Create a reusable PDFBolt proposal template with clientName, projectName, and scope fields. Preview it and save a draft; do not publish it.”
- “List my PDFBolt templates and check my remaining usage. Don't change or render anything.”

The skills are `generate-pdf` and `manage-templates`. No local server, runtime dependencies, or hooks are installed by this plugin.

## OpenAI setup

The supported OpenAI compatibility manifest is `.codex-plugin/plugin.json`. It references the same `skills/` and `.mcp.json` as Claude; there is no second copy of the workflows or backend. This layout is supported by OpenAI's plugin packaging tools. A separate portable root manifest is not needed alongside it.

For ChatGPT developer testing, create an MCP connection to `https://api.pdfbolt.com/mcp`, choose OAuth, and complete PDFBolt sign-in. Test the server connection and the installed skills together in a clean chat. A local Codex installation and a ChatGPT connection are separate test surfaces; success in one does not establish success in the other.

For public submission, use OpenAI's MCP-backed submission path, not Skills only. Reviewer credentials and submission materials belong in the developer portal, not in this package.

## Files, costs, and data

The connector sends the requested HTML, URLs, template data, and conversion options to PDFBolt. URL conversion may fetch the target page and its resources. Template operations read or modify the connected account's templates. Only provide content you are authorized to process.

PDF delivery uses temporary confidential download URLs or embedded PDF resources. Downloading, saving, and visually inspecting them depends on the client's capabilities and permissions. The plugin cannot guarantee local file delivery on every client. HTML authoring requires reliable programmatic UTF-8 Base64 encoding; clients without execution support may need a supplied URL or an existing published template. Switching delivery modes creates another conversion and can consume more credits; explicit user limits take precedence.

Draft changes do not affect published-template conversions until publication. Publishing and deletion require user authorization. The plugin does not need unrelated workspace files or chat history.

Read [PDFBolt's privacy policy](https://pdfbolt.com/privacy) before sending sensitive content. Your client's privacy and data-handling terms also apply.

## Troubleshooting and support

If tools are unavailable, check that PDFBolt is connected and OAuth sign-in completed. For insufficient credits, check usage before trying again. If a PDF cannot be saved, keep its temporary link and check the client's file and network capabilities; do not repeatedly generate the same document.

Contact [contact@pdfbolt.com](mailto:contact@pdfbolt.com) with the client version, tool name, timestamp, and error. Do not send access tokens, confidential PDF URLs, or customer document content.

References: [PDFBolt MCP documentation](https://pdfbolt.com/docs/pdf-mcp-server), [Claude submission checklist](https://claude.com/docs/plugins/pre-submission-checklist), [OpenAI packaging](https://developers.openai.com/plugins/build/plugins), and [OpenAI migration guide](https://developers.openai.com/plugins/guides/submit-claude-plugin).
