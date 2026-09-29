source "https://rubygems.org"

# GitHub Pages gem includes jekyll-feed, jekyll-seo-tag, jekyll-sitemap, etc.
# Note: github-pages gem (v232) has a dependency on commonmarker 0.23 which requires Ruby < 4.0.
# On Ruby 4+, load jekyll and standard GitHub Pages plugins directly.
if RUBY_VERSION >= "4.0"
  gem "jekyll"
  gem "jekyll-feed"
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
  gem "jekyll-paginate"
  gem "jekyll-redirect-from"
  gem "jekyll-gist"
  gem "kramdown"
  gem "kramdown-parser-gfm"
  gem "webrick"
  gem "base64"
else
  gem "github-pages", group: :jekyll_plugins
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :install_if => Gem.win_platform?

gem "bigdecimal"
