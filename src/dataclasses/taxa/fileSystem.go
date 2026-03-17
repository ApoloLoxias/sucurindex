package taxa

import (
	"github.com/ApoloLoxias/sucurindex/src/dataclasses"
	"github.com/google/uuid"
)

type FileSystemE struct {
	ID          uuid.UUID
	Name        string
	Description string
	Root        string
	Mounts      []dataclasses.Link
	Type        string
}
