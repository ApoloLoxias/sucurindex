package taxa

import (
	"github.com/google/uuid"
)

type HostE struct {
	ID          uuid.UUID
	Name        string
	Description string
	OS          string
	HostName    string
	Users       []string
}
