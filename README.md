# Human Message Schema

**Specification Version:** `v0.0.1`  
**Status:** EXPERIMENTAL  

A foundational framing protocol for deterministic speaker attribution in mixed human–agent conversational streams.

> [!WARNING]
> This specification is in active development. Breaking changes to parenthetical attribution semantics are expected.

---

## Grammar

Formal grammar defined in [`schema.ebnf`](schema.ebnf).

```ebnf
message          = human_message | agent_message ;

human_message    = "(" , content , ")" ;
agent_message    = content ;

content          = { character | escaped_char | nested_group } ;
nested_group     = "(" , content , ")" ;
escaped_char     = "\" , ( "(" | ")" | "\" ) ;
character        = ? any Unicode character ? ;
```

### Semantics

- **`human_message`**: A conversational payload bounded by opening and closing parentheses `(` and `)`. Encapsulation denotes explicit provenance from an organic human operator.
- **`agent_message`**: An unadorned conversational payload lacking outer enclosing parentheses. Default attribution assumes automated agent emission.
- **Escaping & Nesting**: Balanced parentheses within human messages are preserved. Escaped parentheses (`\(` and `\)`) may be used to disambiguate literal boundary characters.

## Examples

### Example 1: Standard Turn Exchange
```text
Agent: The meeting has been scheduled.
Human: (my cheeks hurt from grinning, thank you)
```

### Example 2: Inquiry Concerning Protocol Adoption
```text
Human: (Are we putting human messages in parentheses now?)
Agent: Affirmative. Parenthetical containment denotes human provenance.
```

### Example 3: Nested Parenthetical Discourse
```text
Human: (I reviewed the draft (including section 4) and approved it.)
```

## Rationale

In mixed human/agent communication environments, unstructured textual channels lack standardized physical-layer signaling for speaker role. While historical systems relied on out-of-band transport metadata or ad-hoc prefixing (e.g., `User:` vs. `Assistant:`), modern zero-shot interactions require an inline, human-accessible, low-friction delimiter.

Parentheses provide explicit speaker attribution in mixed human/agent communication. By encapsulating human discourse within matching parentheses, agents and downstream parsers can deterministically verify human provenance at the token layer, while preserving unadorned streams for synthetic agent generation.

---

(Schema released. Breaking changes expected.)
