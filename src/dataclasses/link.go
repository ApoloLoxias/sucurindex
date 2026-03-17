package dataclasses

import (
	"github.com/google/uuid"
)

type Link struct {
	Source     uuid.UUID
	Target     uuid.UUID
	Properties []LinkProperty
}

type LinkProperty struct {
	Name  string
	Value string
}
