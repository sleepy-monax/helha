<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8"/>

    <xsl:param name="sortby" select="'day'"/>
    <xsl:param name="order" select="'descending'"/>

    <xsl:param name="startday" select="0"/>

    <xsl:param name="endday" select="9999999999999"/>


    <xsl:template match="/">
        <html>
            <body>
                <table border="1" cellspacing="0" cellpadding="3">
                    <tr bgcolor="#06F">
                        <th>Jour</th>
                        <th>Heure</th>
                    </tr>
                    <xsl:for-each select="accidents/accident[day &gt; $startday and day &lt; $endday]">
                        <xsl:sort select="*[name()=$sortby]" order="{$order}"/>

                        <tr>
                            <td>
                                <xsl:value-of select="day"/>
                            </td>
                            <td>
                                <xsl:value-of select="hour"/>
                            </td>
                            <td>
                                <xsl:value-of select="acct-with-dead-30-days"/>
                            </td>
                            <td>
                                <xsl:value-of select="acct-with-dead"/>
                            </td>
                            <td>
                                <xsl:value-of select="acct-with-mory-inj"/>
                            </td>
                            <td>
                                <xsl:value-of select="acct-with-serly-inj"/>
                            </td>
                            <td>
                                <xsl:value-of select="acct-with-sly-inj"/>
                            </td>
                            <td>
                                <xsl:value-of select="acct"/>
                            </td>

                            <xsl:if test="$lang='fr'">
                                <td>
                                    <xsl:value-of select="adm-dstr-descr-fr"/>
                                </td>
                                <td>
                                    <xsl:value-of select="build-up-area-descr-fr"/>
                                </td>
                                <td>
                                    <xsl:value-of select="coll-type-descr-fr"/>
                                </td>
                                <td>
                                    <xsl:value-of select="day-of-week-descr-fr"/>
                                </td>
                                <td>
                                    <xsl:value-of select="light-cond-descr-fr"/>
                                </td>
                                <td>
                                    <xsl:value-of select="munty-descr-fr"/>
                                </td>
                                <td>
                                    <xsl:value-of select="prov-descr-fr"/>
                                </td>
                                <td>
                                    <xsl:value-of select="rgn-descr-fr"/>
                                </td>
                                <td>
                                    <xsl:value-of select="road-type-descr-fr"/>
                                </td>
                            </xsl:if>

                            <xsl:if test="$lang='nl'">
                                <td>
                                    <xsl:value-of select="adm-dstr-descr-nl"/>
                                </td>
                                <td>
                                    <xsl:value-of select="build-up-area-descr-nl"/>
                                </td>
                                <td>
                                    <xsl:value-of select="coll-type-descr-nl"/>
                                </td>
                                <td>
                                    <xsl:value-of select="day-of-week-descr-nl"/>
                                </td>
                                <td>
                                    <xsl:value-of select="light-cond-descr-nl"/>
                                </td>
                                <td>
                                    <xsl:value-of select="munty-descr-nl"/>
                                </td>
                                <td>
                                    <xsl:value-of select="prov-descr-nl"/>
                                </td>
                                <td>
                                    <xsl:value-of select="rgn-descr-nl"/>
                                </td>
                                <td>
                                    <xsl:value-of select="road-type-descr-nl"/>
                                </td>
                            </xsl:if>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
