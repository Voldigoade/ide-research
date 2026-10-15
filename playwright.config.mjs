import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "./tests",
  testMatch: "**/*.spec.mjs",
  use: { baseURL: "http://127.0.0.1:4173", browserName: "chromium" },
  webServer: {
    command: "python -m http.server 4173 --directory site",
    port: 4173,
    reuseExistingServer: !process.env.CI
  }
});
