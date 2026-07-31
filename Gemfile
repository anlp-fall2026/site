source "https://rubygems.org"

# GitHub Pages gem includes jekyll-feed, jekyll-seo-tag, jekyll-sitemap, etc.
gem "github-pages", group: :jekyll_plugins

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :install_if => Gem.win_platform?

gem "bigdecimal"
