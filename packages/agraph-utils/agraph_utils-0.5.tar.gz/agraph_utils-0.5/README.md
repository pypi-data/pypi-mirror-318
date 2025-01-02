# agraph_utils

## Introduction

`agraph_utils` is a python package that supplies a set of helpful functions
to use along with the `agraph-python` package.

## Installation

```bash
pip install agraph-utils
```

## Usage

### BufferTriples

the BufferTriples class allows the user to quickly add large sets
of triples. You can either add triples individually with `add_triple` 
or you can add a list to the buffer as `add_triples`.

### GeoJSON

This class allows you to easily convert various coordinates of
points/lines/multipolygons into RDF Literals that can be used
for GeoSPARQL.

### Vector Search

This class allows you to easily use the base magic sparql predicates
used in AllegroGraph for vector search. This assumes the user has
a vector store with stored vectors.

