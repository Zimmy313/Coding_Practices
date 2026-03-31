# Command Line Tools (CLT)

wget -E -H -k -K -p https://www.cs.cmu.edu/~15281/coursenotes/mdps/

• -E adds proper filename extensions like .html in some cases
• -H allows spanning to other hosts
• -k rewrites links so the saved page works offline
• -K keeps a backup of original files before link conversion, often as .orig
• -p downloads page requisites like images and CSS

wget -r -l 1 -np -E -k -K -p https://www.cs.cmu.edu/~15281/coursenotes/mdps/