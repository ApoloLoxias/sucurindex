# Document detailing what metadata to store for phase2

## Metadata classes

### Id
Random uuid4 hex, in the format 00000000-0000-0000-0000-00000000 (where 0's are
hex chars) Filename will be {id}.md, and id will be omitted inside the document
to avoid redundancy. Consider duplicating it inside the document if wiki
softwares somehow mess with filenames

### Name
Human-friendly name, using a-z,A-Z,0-9, ,-,_ for characters and not ending on a
trailing whitespace. Does NOT include file extension - extension is tracked via
filetype metadata and path. Defaults to filename without extension.

### Description
Will be stored in the description field, between the first header and the
structured metadata block, for best wiki-software behaviour. Is basically a
free markdown-syntax string. Enforcing linebreaks at 80 characters per line max
could improve human readability.

### Tags
For now, exclusively user generated, using a-z,0-9,-,_ as valid characters.
Case-insensitive - enforced lowercase on input to prevent fragmentation (e.g.
"Work" and "work" would be the same tag).

### Links
Review later, for now:

[uuid | name]<!--direction=outgoing, type=relation_type,-->

uuid and name are metadata fields of the linked taxa. Direction is always
outgoing (for the momment). The whitespaces before and after "|" improve human
legibility and will be enforced for simpler parsing and schema control, as well
as the whitespace after the comma which separetes direction and type. There
will be no characters (including whitespace) between the wikilink and the html
comment and no whitespaces after "<--", nor before "-->". The trailing comma after
type will be enforced, mostly as a way of documenting that we should consider
if we should develop more complex links, with additional properties, in the
future. When parsing [uuid | name], look for the first occurence of "|" or
" | "; although names exlclude this character for now, I see no reason not to
develop a parsing machinery that may be reused in case we expand the available
characters for the alias.

### Missing
Simple boolean flag, true/false.

### Retrieved metadata
For now, we will use mtime and size as metadata retrieved directly from the
file. They will be stored as integers, mtime being the number of seconds since
the start of last unix era and size the number of bytes, for simplicity. In the
future, consider storing more human friendly formats in .md files. Ideas
include ISO timestamps, local time, simply adding "bytes" after size integer to
keep it explicit, or allowing for bytes, bits, KB, KiB, MB, MiB, GB, GiB
concurrently.

### Filetype
The file extension of the artifact, extracted from path. Stored as raw lowercase
string without dot (e.g. "md", "py", "txt"). Semantic grouping is handled via
tags - filetype is for exact extension matching only.

### Path and storage device-related metadata
In development. Will use directional semantic linking and indexed taxa for
storage devices, OS hosts and similar entites

## Metadata ordering
Enforcing a strict order would benefit schema consistency and human
readability. However, it would be best to parse strictly for metadata class
header, ignoring order, to keep the parsing machinery robust and not break
backward compatibility in case of schema ordering change. For now:
Paths/storage > filetype > links > tags > size > mtime > missing