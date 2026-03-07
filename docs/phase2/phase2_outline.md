# Document containing initial plan for phase 2 implementation

---

## 1. Make longterm decisions

### I. Problem statement
The MVP/first phase of the project was exploratory, trying to keep things open,
postpone decisions and embrace inconsistency, i.e. not worring too much about
aesthetics and trying different ways of doing things to see how each of them
would fit together in an integrated system. Now's the time take long lasting
structural decisions.

### II. Crystalize project folder structure

## III. Define and develop metadata schemas for storage and Database construction
Metadata structure, markdown syntax, markdown parsing machinery, database
database structure and searching/querying logic will be developed and versioned
as code is; their development will be an integral part of the project, its
abstract design will be kept somewhat independent from specfic code
implementations and backward compatibility + migration strategies will become
of increasing concern to the SucurIndex's design and evolution (although any
metadata generated in this phase is still expected to be discarded)

### IV. Regularize logging and error handling
The function decorator logging pattern should be enough for now and complex
logging implementations will be postponed to futre phases, but some additional
sophistication and granulity will be usefull moving forward. Error handling
should be standardized, consistent and present on any code written during phase
2

### V. Estabilish and develop coding style conventions and guidelines
The data storage and core logic layers have evolve toward a functional-
adjancent, python-infused style, which seems fit for the expected backend
functionalities. Backend code will, from now on, be thought of in terms of
styling, consistency, performance and aesthetics, and will aspire to be
readable, maintainable, scalable, expandable and pretty. Documentation will
also try to develop and adhere to its own styling guidelines. Style may shift
and evolve throughout the project, but should do so from to active reflection
and intentional setting of goals, not due to the whims of fortune, indiference
towards the preceding conventions, the casuality of absent-minded prose writing
and the randomness of undirected drifts. Front end and user-facing interface
development may benefit from a different style, but its implementation will not
be focused on on phase 2, so its styling will be kept loose, for frontend code
now written is still expected to be discarded and, therefore, must not have
effort spent on beyond the essential.

### VI. Standardize libraries and dependecies, and make their use consistent
Briefly explore different solutions, like os.path and pathlib, to devide on
which should be used

---

## 2. Make something actually usefull

### I. Index and navigate files from multiple devices
This is the original point of the project: to keep a centralized index which 
could be used to search and find files of different

### II. Provide good search functions
Having a comprehensive index is useless if its content is not searchable and
discoverable. This will be made possible by database implementation and the use
of SQL language.

### III. Strive towards a nice visualization and frontend layer
Although actual front end development will be kept away from the current phase,
the metadata generated and stored by the backend function will be made to be
compliant and easily visualized through external and pre-existing organization
software

### IV. Provide versioning and device syncing:
Made possible via integration with git

---

## 3. Integrate with and leverage existing tools:

### I. Implement database layer
- SQLlite seems to be ideal: simple, lightweight,relational and well supported
by python's native libraries
- Define schemas
- Use directional and typed links/edges to create graph-like semantic relations
- Metadata files will continue as the Source of Truth
- Database is to be generated and generated for searching and performance
considerations

### II. GIT
- Staging/reverting changes
- Metadata history
- Disaster recovery
- Used to sync devices using online repositories - consider self hosting
solution due to privacy concerns
- Especially usefull for batch changes and editing metadta files directly
via text editor or wiki software rather than goin through the cli
- After manual edits, check against last comit and list changes/diffs before
commiting

### III. Wiki/notetaking software
- Use for frontend/GUI
- Interesting candidates:
    - Vimwiki
    - Obsidian
    - Logseq
- Keep compatibility, but avoid tieing the project to one specifit solution
and postpone complex integration and development for now

### IV. Store metadata on markdown, rather than TOML
- This is the key for external tool integration
- Markdown is wiki-native and it should be possible to create a format that is
tool-agnostic, working well with VimWiki, Obsidian and LogSeq - its too early
to be tied down to a specific tool
- Markdown is human readable and easily editable
- Easy management/controll with git
- There are good existing python libraries for parsing mardown
- Use CommonMark style
- Consider using wikilinks, due to frontend software functionality
- Use aliasing/html comments to encode information which is to be parsed by the
core logic and database layers, but not really supproted by wiki/frontend (like
typed, directional, semantic links). Example:
"""[uuid|display_name]<!--direction=outgoin, type=inspired_by,-->"""
- Use pure markdown for phase 2, since yaml, frontmatter and similar structures
have some interpretation nuances that change accordian to GUI tool, so I will
steer clear from them for now to remain tool-agnostic
- Developing and using  strict and simple formating/structuring rules will keep
it easy to parse, edit manually and understand visually

---

## 4. Take documentation seriously
Documentation the code itself, as well as future plans and design decisions
should be consistently written and kept from now on.

---

## 5. Inject some personality into the project
To keep development fun and use enjoyable.

---

## 6. Keep learning
- This is my first personal programming project
- This is my first undirected project
- This is my first programming not exclusively in puthon (SQL)
- This is my first project integrating with external, existing software
- This is my first program which I intend to actually use
- This is my biggest/most ambitious project so far
- This is, therefore, a valuable learning experience

---

## 7. Get my feet wet with go and multi-language integration
- In the future, I want a watcher daemon to update metadata when an indexed
file gets its path or filename changed - Go would be ideal for that due to
performance and better/simpler daemonization tools, especially considering
cross OS compatibility
- In this phase, write small golang modules for bulk file i/o with slithering
and DB generation functions - Both important, performance bottlenicking
operations that would benefit greatly from go's concurrency and pre-compiled
performance gains
- Thinking about integrating different languages (compiled and interpreted!)
should be a valuable learning experience, even if this idea is not to see much
further development or even be doomed to getting discarded in the future
- Go/multi-language use is experimental and project may revert to pure Python
or even evolve into pure Go in the future

---

## 8. Summarized roadmap
1. Markdown metadata storage - The foundation for Phase 2 changes
2. SQLite implementation -  Will optimze and expand backend functionality
3. GO experiments - in hopes of better bulk i/o, db generation and future file
system watching/daemon usage
4. Complete the code base with python for the business logic + a simple cli
5. Multi-device support - To be actively embeded on the schemas for #1 and #2
6.. Git and Wiki integration - Should come naturally with #1 and #2

---

"Amphibians invaded the land. Reptiles conquered the skies."