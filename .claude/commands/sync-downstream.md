---
description: Sync downstream OpenShift repository with upstream kubernetes-sigs changes
---

Automate the process of syncing the downstream OpenShift kubernetes-sigs-jobset repository with the upstream kubernetes-sigs/jobset repository.

This command performs the following workflow:
1. Checkout downstream/main as the base
2. Fetch latest changes from both upstream and downstream remotes
3. Create a new sync-downstream branch from upstream/main
4. Merge downstream/main using -s ours strategy to preserve upstream changes
5. Carry over OpenShift-specific files from downstream/main
6. Apply OCP-specific patches to the Makefile
7. Create two commits:
   - "upstream<carry>: Downstream" - for carried files and Makefile patches
   - "upstream<drop>: go mod tidy/vendor" - for go mod operations
8. Leave the branch ready for manual review and push to origin

## Files to carry from downstream

The following OpenShift-specific files/directories should be carried over from downstream/main:
- `.ci-operator.yaml` - OpenShift CI operator configuration
- `.snyk` - Snyk security scanning configuration
- `.tekton/` - Tekton pipeline definitions (entire directory)
- `Dockerfile.ocp` - OpenShift-specific Dockerfile
- `Dockerfile.ci` - CI-specific Dockerfile
- `Makefile-ocp.mk` - OpenShift-specific Makefile
- `renovate.json` - Renovate configuration
- `.gitignore` - OpenShift-specific ignore patterns (removes vendor from ignore)
- `OWNERS` - OpenShift-specific ownership

## Makefile patches to apply

The Makefile should NOT be carried over entirely from downstream. Instead, apply these specific patches to the upstream Makefile:

1. In the `generate` target, comment out the python-sdk generation line and add TODO comment:
   ```makefile
   # TODO: fix python-sdk generation
   # Nevertheless, any changes to the python-sdk should first be pushed to the upstream repo.
   # ./hack/python-sdk/gen-sdk.sh
   ```

2. In the `fmt-verify` target, exclude vendor directory from the find command:
   Change: `@out=\`$(GO_FMT) -w -l -d $$(find . -name '*.go')\`;`
   To: `@out=\`$(GO_FMT) -w -l -d $$(find . -name '*.go' -not -path "./vendor/*")\`;`

3. In the `test` target, remove `test-python-sdk` dependency and add TODO comment:
   ```makefile
   # TODO: add test-python-sdk target
   # Nevertheless, any changes to the python-sdk should first be pushed to the upstream repo.
   .PHONY: test
   test: manifests fmt vet envtest gotestsum
   ```

## Execution Steps

**Important**: Before running this command, ensure:
1. You have git remotes configured:
   - `upstream` pointing to kubernetes-sigs/jobset
   - `downstream` pointing to openshift/kubernetes-sigs-jobset
   - `origin` pointing to your fork of openshift/kubernetes-sigs-jobset
2. You have no uncommitted changes in your working directory
3. You're ready to perform the sync operation

Now perform the downstream sync workflow step by step:

1. First, verify the git remotes are configured correctly by running `git remote -v`
2. Checkout downstream/main: `git checkout downstream/main`
3. Fetch from both remotes: `git fetch downstream` and `git fetch upstream`
4. Create the sync-downstream branch from upstream/main: `git checkout -b sync-downstream upstream/main`
5. Merge downstream/main with -s ours strategy: `git merge -s ours downstream/main` (keeping upstream code but recording downstream history)
6. For each OpenShift-specific file/directory, checkout from downstream/main:
   - Try `git checkout downstream/main -- .ci-operator.yaml` (if error, skip and note)
   - Try `git checkout downstream/main -- .snyk` (if error, skip and note)
   - Try `git checkout downstream/main -- .tekton/` (if error, skip and note)
   - Try `git checkout downstream/main -- Dockerfile.ocp` (if error, skip and note)
   - Try `git checkout downstream/main -- Dockerfile.ci` (if error, skip and note)
   - Try `git checkout downstream/main -- Makefile-ocp.mk` (if error, skip and note)
   - Try `git checkout downstream/main -- renovate.json` (if error, skip and note)
   - Try `git checkout downstream/main -- .gitignore` (if error, skip and note)
   - Try `git checkout downstream/main -- OWNERS` (if error, skip and note)
   - Keep track of which files were successfully carried and which were skipped
7. Apply Makefile patches using the Edit tool:
   - Read the current Makefile
   - Apply patch 1: Comment out `./hack/python-sdk/gen-sdk.sh` in the `generate` target with the TODO comment
   - Apply patch 2: Modify `fmt-verify` to exclude vendor directory
   - Apply patch 3: Remove `test-python-sdk` from `test` target dependencies and add TODO comment
8. Stage all carried files and Makefile changes: `git add -A`
9. Create commit with message: `git commit -m "upstream<carry>: Downstream"`
10. Run `go mod tidy`
11. Run `go mod vendor`
12. Stage the go.mod, go.sum, and vendor/ changes: `git add go.mod go.sum vendor/`
13. Create commit with message: `git commit -m "upstream<drop>: go mod tidy/vendor"`
14. Display the branch status and summary of what was done

After completion, remind the user to:
- Review the changes with: `git log --oneline -10` and `git diff downstream/main`
- Check the carried files look correct
- Verify the Makefile patches were applied correctly
- If satisfied, push to your fork with: `git push --set-upstream origin sync-downstream`
- Create a pull request targeting downstream/main in the openshift/kubernetes-sigs-jobset repository

Handle errors gracefully:
- If remotes don't exist, provide clear instructions on how to add them
- If there are uncommitted changes, warn the user and stop
- If merge conflicts occur during the -s ours merge, explain and provide guidance
- If a file doesn't exist in downstream/main during checkout, catch the error, skip it, and note which files were skipped
- If Makefile patching fails, show the error and provide manual instructions
- If go mod commands fail, show the error and stop
- Display a summary at the end showing which files were carried and which were skipped