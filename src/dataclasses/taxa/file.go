package taxa

import (
	"github.com/ApoloLoxias/sucurindex/src/dataclasses"
	"github.com/google/uuid"
)

type FileE struct {
	ID          uuid.UUID
	Name        string
	Description string
	Paths       []string
	Links       []dataclasses.Link
	Tags        []string
	Size        int
	Mtime       int
	Missing     bool
}
