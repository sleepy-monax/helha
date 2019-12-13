<?php
extension_loaded('apc');
include_once('accident.php');

class Accidents
{
    private static $_the;

    public $all;

    public $day_of_week;
    public $area;
    public $colltype;
    public $lightcond;
    public $roadtype;
    public $provinces;
    public $regions;
    public $communes;

    public static function the()
    {
        if (is_null(self::$_the) && apcu_exists("accidents")) {
            self::$_the = apcu_fetch("accidents");
        }

        if (is_null(self::$_the)) {
            self::$_the = new Accidents('/data/accidents.xml');
            apcu_store("accidents", self::$_the);
        }

        return self::$_the;
    }

    private function __construct($path)
    {
        $xml = simplexml_load_file($_SERVER['DOCUMENT_ROOT'] . $path, null, LIBXML_COMPACT);

        $this->all = array();

        foreach ($xml->children() as $child) {
            array_push($this->all, new Accident($child));

            $this->day_of_week[(string) $child->{'day-of-week'}] = array(
                'fr' => (string) $child->{'day-of-week-descr-fr'},
                'nl' => (string) $child->{'day-of-week-descr-nl'},
            );

            $this->area[(string) $child->{'build-up-area'}] = array(
                'fr' => (string) $child->{'build-up-area-descr-fr'},
                'nl' => (string) $child->{'build-up-area-descr-nl'},
            );

            $this->colltype[(string) $child->{'coll-type'}] = array(
                'fr' => (string) $child->{'coll-type-descr-fr'},
                'nl' => (string) $child->{'coll-type-descr-nl'},
            );

            $this->lightcond[(string) $child->{'light-cond'}] = array(
                'fr' => (string) $child->{'light-cond-descr-fr'},
                'nl' => (string) $child->{'light-cond-descr-nl'},
            );

            $this->roadtype[(string) $child->{'road-type'}] = array(
                'fr' => (string) $child->{'road-type-descr-fr'},
                'nl' => (string) $child->{'road-type-descr-nl'},
            );

            $this->provinces[(string) $child->{'prov-refnis'}] = array(
                'fr' => (string) $child->{'prov-descr-fr'},
                'nl' => (string) $child->{'prov-descr-nl'},
            );

            $this->regions[(string) $child->{'rgn-refnis'}] = array(
                'fr' => (string) $child->{'rgn-descr-fr'},
                'nl' => (string) $child->{'rgn-descr-nl'},
            );

            $this->communes[(string) $child->{'munty-refnis'}] = array(
                'fr' => (string) $child->{'munty-descr-fr'},
                'nl' => (string) $child->{'munty-descr-nl'},
            );
        }
    }
}
