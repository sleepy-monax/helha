<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8"/>

    <xsl:template match="stages">
        <html>
            <body>
                <xsl:apply-templates select="stage"/>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="stage">
        <p>
            <xsl:value-of select="fonction"/>
            <xsl:apply-templates select="etudiant"/>
            <xsl:apply-templates select="entreprise"/>
        </p>
    </xsl:template>

    <xsl:template match="etudiant">
        <div>
            Nom:&#160;<xsl:value-of select="nom"/>
        </div>
        <div>
            Prenom:&#160;<xsl:value-of select="prenom"/>
        </div>
        <div>
            Section:&#160;<xsl:value-of select="section"/>
        </div>
        <div>
            Classe:&#160;<xsl:value-of select="classe"/>
        </div>
    </xsl:template>

    <xsl:template match="entreprise">
    </xsl:template>
</xsl:stylesheet>
