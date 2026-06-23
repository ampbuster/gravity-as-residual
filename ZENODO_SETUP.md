# Zenodo Setup Guide for gravity-as-residual

This is the step-by-step walkthrough for publishing `gravity-as-residual` on Zenodo with a citable DOI.

## What you'll get

- A DOI for the v3.5.9-A2 release (e.g., `10.5281/zenodo.12345678`)
- A DOI badge in the README
- Permanent archive of all files in the release
- Auto-archive for future releases (just make a new release)

---

## Step 1: Sign in to Zenodo

1. Go to **https://zenodo.org**
2. Click **Log in** (top right)
3. Choose **Log in with GitHub**
4. Authorize Zenodo to access your GitHub account

---

## Step 2: Enable the repository

1. Once logged in, click your **profile picture** (top right) → **Settings**
2. In the left sidebar, click **GitHub**
3. You'll see a list of your GitHub repos
4. Find **`ampbuster/gravity-as-residual`** in the list
5. Flip the **switch ON** next to it (it should turn green)
6. (Optional) Click the **gear icon** to configure:
   - **Release tag prefix**: leave default (no prefix)
   - **Custom branch**: leave default (main)
   - **Enabled**: ON

> Zenodo is now connected. It will watch for new GitHub releases.

---

## Step 3: Create the GitHub release

1. Go to your GitHub repo: **https://github.com/ampbuster/gravity-as-residual**
2. Click **Releases** (right sidebar, or go to `/releases`)
3. Click **Create a new release** (or **Draft a new release**)
4. Fill in:
   - **Choose a tag**: type `v3.5.9-A2` and select **Create new tag: v3.5.9-A2 on publish**
   - **Target**: `main`
   - **Release title**: `v3.5.9-A2 — L308ce Audit`
   - **Description**: paste the release notes (see `RELEASE_NOTES_v3.5.9-A2.md`)
5. Click **Publish release**

---

## Step 4: Wait for Zenodo to archive

- Within ~5 minutes, Zenodo will detect the release
- It will create a Zenodo record and a DOI
- You'll get an email from Zenodo with the new DOI
- Or check https://zenodo.org/account/settings/github/ to see the new record

---

## Step 5: Add DOI badge to README

Once you have the DOI, add this to the top of `README.md` (right after the title):

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```

(Replace `XXXXXXX` with the actual Zenodo record number.)

---

## Step 6: Cite the paper

Now you can cite the paper as:

> Lee, Jia Ray. (2026). Gravity as Residual: A Geometric Framework for the Dark Sector via Scale-Invariant Dimensional Cascades (v3.5.9-A2). Zenodo. https://doi.org/10.5281/zenodo.20810441

Update `CITATION.cff` with the DOI as well.

---

## Future releases

For every future release (e.g., `v3.5.10`, `v3.6.0`):

1. Bump version in code
2. Update README and CHANGELOG
3. Commit, push, then create a new GitHub release with a new tag
4. Zenodo auto-creates a new DOI for that release
5. Each release is independently citable

The "latest" DOI will point to the most recent release. Older releases keep their own DOIs (versioned citation).

---

## Troubleshooting

### Zenodo didn't pick up the release

- Check Settings → GitHub → the integration is enabled
- Wait up to 15 minutes (sometimes Zenodo is slow)
- Check the release is published (not a draft)
- Re-trigger by making a tiny edit to the release notes and saving

### Wrong files archived

- Zenodo archives the **state of the repo at the release tag**
- The tag must be on a specific commit, not a branch
- To re-archive: delete the GitHub release, recreate it on the same commit

### Want a separate DOI for the arxiv paper only

See `ZENODO_ARXIV_PAPER.md` for the manual upload approach (Option A).

---

## Files in this directory

- `ZENODO_SETUP.md` (this file) — the walkthrough
- `RELEASE_NOTES_v3.5.9-A2.md` — release notes to paste into GitHub
- `ZENODO_ARXIV_PAPER.md` — optional manual upload guide for the arxiv paper
