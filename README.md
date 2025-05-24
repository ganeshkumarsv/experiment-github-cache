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

## Project Structure

- `src/main.py`: Python script that generates timestamps for cache testing
- `.github/workflows/main-branch-cache.yml`: Workflow for testing cache sharing within main branch
- `.github/workflows/feature-branch-cache.yml`: Workflow for testing cache sharing between main and feature branches

## How to Run

1. Push to main branch to create initial cache
2. Create a feature branch (e.g., `feature-test`)
3. Push to feature branch to test cache sharing
4. Check workflow runs in GitHub Actions to see the results
