# ManuForm Keyboard

These are the design files for my custom ManuForm keyboard.

## FreeCAD script(s)

./ManuForm1.py is a python script that I used with [FreeCAD](http://www.freecadweb.org/wiki/?title=Download) to parametrically/programattically generate the "keywells" of the keyboard.  FreeCAD is free and open source, and is pretty cool. It's still under development though and not quite full-featured, IMO (at time of writing).


## Silo save files

Then, I imported that shape into [Silo](http://www.nevercenter.com/silo/). Silo is a 3D modelling program. It's nice because it *doesn't* do anything else like texturing, bones/rigging/animation, etc. It *just* does modelling. But it's a very very good modelling program, IMO, and it's only about $100. Prior to that, I professionally used 3DSMax, which costs on the order of multiple thousands of dollars, and I would have to use many plugins including custom plugins I wrote myself just to get all the modelling tools I needed, but with Silo, it just works off the shelf. If all you need is to make a shape, it's the best (and cheapest) way to go. /rant

So all of my silo incremental save files are here too, including ./ManuFormMark2_020.sib which is the latest and the one that I used to export the final model.


## Export Process

After exporting the .stl file from Silo, I ran it through [netfabb](http://www.netfabb.com/) to clean up the model, fix the scaling, fix holes, fix manifold errors, etc. The basic version of netfabb is freeware, and has the automatic repair which is all you need for this.


## Shapeways

Then, with the repaired .stl file from netfabb, I uploaded it to [shapeways](http://www.shapeways.com/product/6BNKXTXTA/manuform-keyboard?key=9d07b99823474e036abe511d064ed4b0) and had them print it. This link is to my "product" on shapeways so you could go and print my version from here: [ManuForm Keyboard](http://www.shapeways.com/product/6BNKXTXTA/manuform-keyboard?key=9d07b99823474e036abe511d064ed4b0).
