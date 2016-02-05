library("GEOquery")

# Primera descarga

getGEO(GEO = "GSE6613",GSEMatrix = TRUE,destdir = ".")

GSE6613<-read.csv(gzfile("GSE6613_series_matrix.txt.gz"),
                   comment.char = "!", 
                   sep = "\t",
                   stringsAsFactors = FALSE)

dim(GSE6613)

# Segunda descarga

getGEO(GEO = "GSE8397",GSEMatrix = TRUE,destdir = ".")

GSE8397<-read.csv(gzfile("GSE8397-GPL96_series_matrix.txt.gz"),
                  comment.char = "!", 
                  sep = "\t",
                  stringsAsFactors = FALSE)

dim(GSE8397)

# Tercera descarga

getGEO(GEO = "GSE20164",GSEMatrix = TRUE,destdir = ".")

GSE20164<-read.csv(gzfile("GSE20164_series_matrix.txt.gz"),
                  comment.char = "!", 
                  sep = "\t",
                  stringsAsFactors = FALSE)

dim(GSE20164)
