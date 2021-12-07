class Panoply < Formula
  include Language::Python::Virtualenv

  desc "Panoply: save your commands and reuse them."
  homepage "https://github.com/jeremynac/panoply"
  url "panoply_homebrew_formula_url"
  sha256 "27a1d8d2820eed4e079f80260e5d6f3ecb00f4c8cf8a25692679ff4ae38a0979"

  depends_on "python3"

  panoply_homebrew_formula_resources

  def install
    virtualenv_create(libexec, "python3")
    virtualenv_install_with_resources
  end

  test do
    false
  end
end
