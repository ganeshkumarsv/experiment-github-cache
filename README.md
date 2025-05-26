# GitHub Cache Sharing Experiment

This repository demonstrates how GitHub caches are shared and isolated across branches in various scenarios.

## Scenarios

### 1. Cache Sharing within Branches

This scenario tests cache sharing within the main branch:
- The workflow creates a cache with a timestamp
- A subsequent workflow run on the same branch restores this cache

To test:
1. Push to the main branch or manually trigger the workflow
2. The workflow will create a cache with a timestamp
3. Trigger the workflow again to see the cache being restored

### 2. Cache Sharing between Base and Feature Branches

This scenario tests cache sharing between main and feature branches:
- Create cache on the main branch
- Create a feature branch and verify it can access the cache from main

To test:
1. Push to the main branch to create the initial cache
2. Create a new branch named `feature-test` from main
3. Push to the feature branch to trigger the workflow
4. The workflow will attempt to restore the cache from main

### 3. Cache Isolation between Sibling Branches

This scenario tests cache isolation between sibling branches:
- Create two feature branches (feature-a and feature-b) from main
- Verify that caches created on one feature branch are not accessible from the other

To test:
1. Create branch `feature-a` from main and push to it
2. Create branch `feature-b` from main and push to it
3. Each branch will create its own cache
4. Verify that the caches are isolated between the branches

### 4. Cache Sharing for Pull Requests

This scenario tests cache sharing in pull requests:
- Create a feature branch (feature-a) from main
- Create another branch (feature-b) from feature-a
- Create a PR from feature-b to feature-a
- Verify cache access from both main and base branches

To test:
1. Create branch `feature-a` from main and push to it
2. Create branch `feature-b` from feature-a and push to it
3. Create a PR from feature-b to feature-a
4. The workflow will attempt to restore caches from both main and feature-a

## Project Structure

- `src/main.py`: Python script that generates timestamps for cache testing
- `.github/workflows/main-branch-cache.yml`: Workflow for testing cache sharing within main branch
- `.github/workflows/feature-branch-cache.yml`: Workflow for testing cache sharing between main and feature branches
- `.github/workflows/sibling-branch-cache.yml`: Workflow for testing cache isolation between sibling branches
- `.github/workflows/pr-cache.yml`: Workflow for testing cache sharing in pull requests

## How to Run

1. Push to main branch to create initial cache
2. Create feature branches as described in each scenario
3. Create pull requests as needed
4. Check workflow runs in GitHub Actions to see the results
