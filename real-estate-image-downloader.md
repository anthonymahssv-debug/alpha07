---
name: real-estate-image-downloader
description: Extract and download property photos from public real estate listing links with built-in intelligence for three Santa Fe CDMX towers — Paradox, Torre 300, and Península Tower 546. Produces unit-level galleries, tower-level visual libraries, a consolidated CSV manifest, and a zip bundle ready for ingestion into the SF 546 CI intelligence platform.
license: MIT
metadata:
  version: "2.0"
  primary_targets: ["inmuebles24.com", "lamudi.com.mx"]
  tower_scope: ["paradox", "torre-300", "peninsula-546"]
  downstream_platform: "SF 546 CI"
---

# Real Estate Image Downloader — v2.0

## Purpose

Extract and download property photos from public real estate listing links for Santa Fe CDMX towers, classify them as interior/exterior, deduplicate them, generate a manifest, and package the output as a zip bundle.

Use only public pages. Do not bypass login, paywalls, captcha, robots.txt, or site restrictions.

## Tower Scope

### Paradox Santa Fe

- Variants: `Paradox`, `Torre Paradox`, `Paradox Santa Fe`
- Address signal: `Javier Barros Sierra`
- Canonical tag: `paradox`

### Torre 300

- Variants: `Torre 300`, `Torre300`, `T300`
- Address signal: `Javier Barros Sierra 300`
- Canonical tag: `torre-300`

### Península Tower 546

- Variants: `Península`, `Peninsula`, `Península Santa Fe`, `Península Tower 546`, `Peninsula 546`
- Address signal: `Javier Barros Sierra 546`
- Canonical tag: `peninsula-546`

## Tower Detection Rules

Detect tower from:

1. Page title and H1.
2. Listing description.
3. Address field.
4. Breadcrumb/neighborhood tags.
5. URL slug.

If no tower matches, tag as `out-of-scope`.

## Modes

### Mode A — Single Unit

Input: one listing URL.  
Output: one unit gallery split into interior/exterior folders.

### Mode B — Batch Units

Input: multiple listing URLs.  
Output: per-listing folders, manifest CSV, and zip bundle.

### Mode C — Tower Aggregation

Input: tower name or multiple listings for the same tower.  
Output: deduplicated tower-level visual library.

## Image Classification

### Interior

Classify as `interior` if image shows:

- sala
- comedor
- cocina
- recámara
- baño
- vestidor
- estudio
- office
- laundry
- indoor gym
- spa room
- cinema room
- co-working lounge
- indoor finishes

### Exterior

Classify as `exterior` if image shows:

- fachada
- tower silhouette
- skyline
- entrance
- motor lobby
- drop-off
- pool deck
- rooftop terrace
- garden
- paddle court
- balcony/view
- aerial/site plan
- outdoor amenities

### Unclear

Use `unclear` when classification is not reliable.

## Output Folder Structure

```text
sf546-images/
├── paradox/
│   ├── tower/
│   │   ├── interior/
│   │   └── exterior/
│   └── units/
├── torre-300/
│   ├── tower/
│   │   ├── interior/
│   │   └── exterior/
│   └── units/
├── peninsula-546/
│   ├── tower/
│   │   ├── interior/
│   │   └── exterior/
│   └── units/
├── out-of-scope/
│   └── units/
└── manifest.csv
