#!A:\Xampp\perl\bin\perl.exe
# The above line is perl execution path in xampp
# The below line tells the browser, that this script will send html content.
# If you miss this line then it will show "malformed header from script" error.

# Place the CGI file in a folder called apheleia 
# Create a folder named 'pastes/'
# http://localhost/apheleia/apheleia.cgi -> this will open the website
# http://localhost/apheleia/pastes/XXXXX.txt -> paste will be saved in a similar URL

use strict;
use warnings;

use CGI qw(:standard);
use Digest::MD5 qw(md5_hex);

my $paste_dir = "pastes/";

print header();
print start_html(
    -title => 'Apheleia',
    -style => {
        -src => 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
        -integrity => 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T',
        -crossorigin => 'anonymous'
    }
);

if (param('paste')) {
    my $paste = param('paste');
    my $filename;
    do {
        $filename = $paste_dir . md5_hex(rand() . time() . $$ . rand() . rand()) . ".txt";
    } while (-e $filename);
    open(my $fh, ">", $filename) or die "Cannot open file: $!";
    print $fh $paste;
    close($fh);

    print "<div class=\"container\"><div class=\"alert alert-success mt-3\" role=\"alert\">Your paste has been saved. Here's the link: <a href=\"$filename\">$filename</a></div></div>";
}
else {
    print <<HTML;
<div class="container">
    <h1 class="mt-3">Apheleia</h1>
    <form method="POST">
        <div class="form-group">
            <label for="paste">Paste your code:</label>
            <textarea id="paste" name="paste" rows="10" class="form-control"></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</div>
HTML
}

print end_html();
