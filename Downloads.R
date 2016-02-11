library("GEOquery")

# Parkinson (GPL96)
# --1--
getGEO(GEO = "GSE35642",GSEMatrix = TRUE,destdir = ".")
GSE35642<-read.csv(gzfile("GSE35642_series_matrix.txt.gz"),
                   comment.char = "!", 
                   sep = "\t",
                   stringsAsFactors = FALSE)
# --2--
getGEO(GEO = "GSE20186",GSEMatrix = TRUE,destdir = ".")
GSE20186<-read.csv(gzfile("GSE20186-GPL96_series_matrix.txt.gz"),
                   comment.char = "!", 
                   sep = "\t",
                   stringsAsFactors = FALSE)
# --3--
getGEO(GEO = "GSE20314",GSEMatrix = TRUE,destdir = ".")
GSE20314<-read.csv(gzfile("GSE20314_series_matrix.txt.gz"),
                   comment.char = "!", 
                   sep = "\t",
                   stringsAsFactors = FALSE)
# --dimensiones--
dim(GSE35642)
dim(GSE20186)
dim(GSE20314)

# Alzheimer (GPL570)
# --1--
getGEO(GEO = "GSE66333",GSEMatrix = TRUE,destdir = ".")
GSE66333<-read.csv(gzfile("GSE66333_series_matrix.txt.gz"),
                   comment.char = "!", 
                   sep = "\t",
                   stringsAsFactors = FALSE)
# --2--
getGEO(GEO = "GSE48350",GSEMatrix = TRUE,destdir = ".")
GSE48350<-read.csv(gzfile("GSE48350_series_matrix.txt.gz"),
                   comment.char = "!", 
                   sep = "\t",
                   stringsAsFactors = FALSE)
# --3--

getGEO(GEO = "GSE53890",GSEMatrix = TRUE,destdir = ".")
GSE53890<-read.csv(gzfile("GSE53890_series_matrix.txt.gz"),
                   comment.char = "!", 
                   sep = "\t",
                   stringsAsFactors = FALSE)
# --dimensiones--

dim(GSE66333)
dim(GSE48350)
dim(GSE53890)

# Esclerosis Multiple (GPL570)
# --1--
getGEO(GEO = "GSE68527",GSEMatrix = TRUE,destdir = ".")
GSE68527<-read.csv(gzfile("GSE68527_series_matrix.txt.gz"),
                   comment.char = "!", 
                   sep = "\t",
                   stringsAsFactors = FALSE)
# --2--
getGEO(GEO = "GSE59085",GSEMatrix = TRUE,destdir = ".")
GSE59085<-read.csv(gzfile("GSE59085_series_matrix.txt.gz"),
                   comment.char = "!", 
                   sep = "\t",
                   stringsAsFactors = FALSE)
# --3--
getGEO(GEO = "GSE37783",GSEMatrix = TRUE,destdir = ".")
GSE37783<-read.csv(gzfile("GSE37783_series_matrix.txt.gz"),
                   comment.char = "!", 
                   sep = "\t",
                   stringsAsFactors = FALSE)
# --dimensiones--
dim(GSE68527)
dim(GSE59085)
dim(GSE37783)
