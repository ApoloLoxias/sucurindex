package dataclasses

import (
	"fmt"

	"github.com/google/uuid"
)

type MetadataS struct {
	Kind  string
	Value []string
}

type MetadataV interface {
	MetadataS() MetadataS
}

type MetadataStr struct {
	Kind  string
	Value string
}

func (md MetadataStr) MetadataS() MetadataS {
	return MetadataS{Kind: md.Kind, Value: []string{md.Value}}
}

type MetadataInt struct {
	Kind  string
	Value int
}

func (md MetadataInt) MetadataS() MetadataS {
	return MetadataS{Kind: md.Kind, Value: []string{fmt.Sprintf("%d", md.Value)}}
}

type MetadataBool struct {
	Kind  string
	Value bool
}

func (md MetadataBool) MetadataS() MetadataS {
	return MetadataS{Kind: md.Kind, Value: []string{fmt.Sprintf("%t", md.Value)}}
}

type MetadataStrS struct {
	Kind  string
	Value []string
}

func (md MetadataStrS) MetadataS() MetadataS {
	return MetadataS{Kind: md.Kind, Value: md.Value}
}

type ID struct {
	Value uuid.UUID
}

func (id ID) MetadataS() MetadataS {
	return MetadataS{Kind: "ID", Value: []string{id.Value.String()}}
}

type MetadataLinkS struct {
	Value []Link
}

func (md MetadataLinkS) MetadataS() MetadataS {
	Kind := "Links"
	strs := []string{}
	links := md.Value

	if len(links) != 0 {
		for _, link := range links {
			strs = append(strs, link.String())
		}

	}
	return MetadataS{Kind: Kind, Value: strs}
}
