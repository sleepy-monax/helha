<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8"/>
    
    <xsl:template match="Bottin">
        <html>
            <head>
                <title>
                    Botin&#160;-&#160;<xsl:value-of select="@region"/>
                </title>
            </head>
            <body>
                <xsl:apply-templates select="Abonne"/> 
            </body>
        </html>
    </xsl:template>
    
    <xsl:template match="Abonne">
        <h1 align="center">
            <xsl:value-of select="@id"/>&#160;<xsl:value-of select="Nom"/>&#160;<xsl:value-of select="Prenom"/>
        </h1>
        <p align="center">
            <font size="5" color="red">
                TELEPHONE:<xsl:value-of select="Tel"/>
            </font>
        </p>
        <h3 align="center">
            <xsl:apply-templates select="Adresse"/>
        </h3>
        <HR/>
    </xsl:template>
    
    <xsl:template match="Adresse">
        <h3 align="center">
            <xsl:value-of select="codepostal"/>
            <xsl:value-of select="designation"/>&#160;
            <xsl:value-of select="Adresse-nom"/>&#160;
            N°&#160;<xsl:value-of select="numero"/>&#160;
        </h3>
    </xsl:template>
</xsl:stylesheet>
