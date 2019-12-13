<?php
class Accident
{
    public $day;
    public $hour;
    public $dayofweek;
    public $area;
    public $colltype;
    public $lightcond;
    public $roadtype;
    public $province;
    public $region;
    public $commune;

    public $acct;
    public $acct_with_dead_30_days;
    public $acct_with_dead;
    public $acct_with_mory_inj;
    public $acct_with_serly_inj;
    public $acct_with_sly_inj;

    public function __construct($xml_node)
    {
        $this->day = (int) $xml_node->{'day'};
        $this->hour = (int) $xml_node->{'hour'};
        $this->dayofweek = (int) $xml_node->{'day-of-week'};
        $this->area = (int) $xml_node->{'build-up-area'};
        $this->colltype = (int) $xml_node->{'coll-type'};
        $this->lightcond = (int) $xml_node->{'light-cond'};
        $this->roadtype = (int) $xml_node->{'road-type'};
        $this->province = (int) $xml_node->{'prov-refnis'};
        $this->region = (int) $xml_node->{'rgn-refnis'};
        $this->commune = (int) $xml_node->{'munty-refnis'};

        $this->acct = (int) $xml_node->{'acct'};
        $this->acct_with_dead_30_days = (int) $xml_node->{'acct-with-dead-30-days'};
        $this->acct_with_dead = (int) $xml_node->{'acct-with-dead'};
        $this->acct_with_mory_inj = (int) $xml_node->{'acct-with-mory-inj'};
        $this->acct_with_serly_inj = (int) $xml_node->{'acct-with-serly-inj'};
        $this->acct_with_sly_inj = (int) $xml_node->{'acct-with-sly-inj'};
    }
}
