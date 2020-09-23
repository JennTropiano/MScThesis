run("Colour Deconvolution", "vectors=Azan-Mallory"); // make colour

close(); 							// close colour 3 window
setAutoThreshold("Default dark");
run("Threshold...");
setThreshold(128, 252);
setOption("BlackBackground", false);
run("Convert to Mask");
run("Close");						// close threshold window
// DEFAULT VALUES 
processed_dir_name = "Processed" // Just meaning they are done
processed_file_suffix = "processed.jpg" // tells me it has actually gone through it all

dir="C:Users/Jenn/Documents/Thesis/RILs Screening/"
stripName = substring(File.name, 0, indexOf(File.name, "."));  

title = getTitle()
//saveAs("Jpeg", dir+stripName+"-"+processed_file_suffix);
saveAs("PNG", dir+title+"-"+processed_file_suffix);

close();
close();
close();
close();
