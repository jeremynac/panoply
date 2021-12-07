cp panoply_template.rb formula/panoply.rb
sed -i "s/panoply_homebrew_formula_url/https:\/\/pypi.io\/packages\/source\/p\/panoply\/panoply-$1.tar.gz/" formula/panoply.rb

