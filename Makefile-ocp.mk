include Makefile

.PHONY: verify-ocp
verify-ocp: manifests
	@if !(git diff --quiet HEAD); then \
		git diff; \
		echo "manifests are out of date, run make manifests"; exit 1; \
	fi

.PHONY: build-ocp
build-ocp: fmt vet
	$(GO_BUILD_ENV) $(GO_CMD) build -ldflags="$(LD_FLAGS)" -o bin/manager main.go
