import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

# Combined array: Your 4 visual images + all original gallery images
combined_array_code = 'const insomniacImages = ["./visual-01.jpeg", "./visual-02.jpeg", "./visual-03.jpeg", "./visual-04.jpeg", "mischiefmanagediidraft1.png", "8.debunkingmyths.png", "safarnama.png", "5.mumbai-colorgrading.png", "de57b5f1-9795-4d6d-a063-062ef8a4ee59.jpeg", "d95bb0c2-546c-494c-b40f-0e47506f1a4c.jpeg", "valentinespecialpost.png", "fukcaverageposter.jpg", "1dad6dae-ed67-4d04-86a3-b5cfa019f38f.jpeg", "7.3.dusummervacation.png", "e69df499-dd26-4d02-9eb8-9b7bd40e0505.jpeg", "47a7f269-a9af-4309-a72e-d0120a24d8ea.jpeg", "4031e24f-8d86-4a19-840d-a57f91107b10_1_201_a.jpeg", "2.beyondthehypei3-tiler.png", "2(2).jpg", "ammm.png", "5.histrionicajudges.png", "1.charades.png", "1(1).png", "7.jpeg", "1.1.prajaktakoliibooklaunch(1).png", "12.png", "9.invitationithefinalhand.png", "2e3cb980-6afb-49e3-9f5d-7cea9943c17a.jpeg", "7.2.dusummervacation.png", "1.mschficarousel.png", "1.stillrollin’.png", "7.1.dusummervacation.png", "7.4.dusummervacation.png", "3.evocusidramsoc.png", "1.1.priyanshumodiistandeeihistrionica.png", "20.jpg", "1(2).png", "22.png", "4.sharktankpanelibizstreet.png", "rntl..png", "23.jpg", "f64a91b4-1d10-4ea2-b8fd-6b5ca2825475_1_105_c.jpeg", "13.1.giveaway(1).jpg", "64740a27-7c2f-4e74-a84a-6717f5918fe9_1_105_c.jpeg", "24fb5243-7a38-45aa-88ff-e6742ee477bc.jpeg", "2.playstationicrossroads.png", "19.jpg", "xkmnk.png", "093b1d12-3f48-4208-a33c-0d3f9adfb345.jpeg", "262daae1-dd64-4200-9d3a-26310da58f34_1_105_c.jpeg", "2.raahwarga.png", "chance.jpg", "lalalalalala.png", "7.festiveseasonibrandsicarousel.png", "2.png", "5d27e539-02e0-4930-be55-030e03e58d27.jpeg", "1.jpg", "1.png", "13.2.giveaway.jpg", "3.zomatoiassignmentpost.png"];'

pattern = r'const insomniacImages = \[[\s\S]*?\];'

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    if re.search(pattern, content):
        content = re.sub(pattern, combined_array_code, content, count=1)
        with open(t, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated insomniacImages to combined list in {t}")
    else:
        print(f"Warning: insomniacImages pattern not found in {t}")

print("Combined visual images update complete!")
