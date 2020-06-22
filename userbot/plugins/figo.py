@bot.on(dev_cmd(pattern="figo", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "figo":
    await event.edit("figo")
    animation_chars = [

            "L_",

            "LO_",

            "LOR_",

            "LORE_",
            
            "LORE _",
            
            "LORE È_",
            
           "LORE È _", 
           
           "LORE È U_",
           
           "LORE È UN_",
           
           "LORE È UN _",
           
           "LORE È UN F_",
           
           "LORE È UN FI_",
           
           "LORE È UN FIG_",
           
           "LORE È UN FIGO",

        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 10])