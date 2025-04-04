"""Description for all supported Entities."""

from __future__ import annotations

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
)
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.components.switch import SwitchDeviceClass
from homeassistant.const import PERCENTAGE, EntityCategory, UnitOfTime

from .descriptions_definitions import (
    HCBinarySensorEntityDescription,
    HCButtonEntityDescription,
    HCEntityDescription,
    HCNumberEntityDescription,
    HCSelectEntityDescription,
    HCSensorEntityDescription,
    HCSwitchEntityDescription,
)

ENTITY_DESCRIPTIONS: dict[str, list[HCEntityDescription]] = {
    "abort_button": [
        HCButtonEntityDescription(
            key="button_abort_program",
            entity="BSH.Common.Command.AbortProgram",
        )
    ],
    "active_program": [
        HCSensorEntityDescription(
            key="sensor_active_program",
            entity="BSH.Common.Root.ActiveProgram",
            device_class=SensorDeviceClass.ENUM,
            has_state_translation=True,
        )
    ],
    "binary_sensor": [
        HCBinarySensorEntityDescription(
            key="binary_sensor_door_state",
            entity="BSH.Common.Status.DoorState",
            device_class=BinarySensorDeviceClass.DOOR,
            value_on={"Open"},
            value_off={"Closed"},
        ),
        HCBinarySensorEntityDescription(
            key="binary_sensor_door_state",
            entity="Refrigeration.Common.Status.Door.Freezer",
            device_class=BinarySensorDeviceClass.DOOR,
            value_on={"Open"},
            value_off={"Closed"},
        ),
        HCBinarySensorEntityDescription(
            key="binary_sensor_door_state",
            entity="Refrigeration.Common.Status.Door.Refrigerator",
            device_class=BinarySensorDeviceClass.DOOR,
            value_on={"Open"},
            value_off={"Closed"},
        ),
        HCBinarySensorEntityDescription(
            key="binary_sensor_eco_dry_active",
            entity="Dishcare.Dishwasher.Status.EcoDryActive",
            entity_registry_enabled_default=False,
        ),
        HCBinarySensorEntityDescription(
            key="binary_sensor_aqua_stop",
            device_class=BinarySensorDeviceClass.PROBLEM,
            entity="BSH.Common.Event.AquaStopOccured",
            entity_registry_enabled_default=False,
            value_on={"Present"},
            value_off={"Off", "Confirmed"},
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        HCBinarySensorEntityDescription(
            key="binary_sensor_low_water_pressure",
            device_class=BinarySensorDeviceClass.PROBLEM,
            entity="BSH.Common.Event.LowWaterPressure",
            entity_registry_enabled_default=False,
            value_on={"Present"},
            value_off={"Off", "Confirmed"},
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
    ],
    "event_sensor": [
        HCSensorEntityDescription(
            key="sensor_rinse_aid",
            entities=[
                "Dishcare.Dishwasher.Event.RinseAidLack",
                "Dishcare.Dishwasher.Event.RinseAidNearlyEmpty",
            ],
            device_class=SensorDeviceClass.ENUM,
            options=["empty", "nearly_empty", "full"],
        ),
        HCSensorEntityDescription(
            key="sensor_salt",
            entities=[
                "Dishcare.Dishwasher.Event.SaltLack",
                "Dishcare.Dishwasher.Event.SaltNearlyEmpty",
            ],
            device_class=SensorDeviceClass.ENUM,
            options=["empty", "nearly_empty", "full"],
        ),
    ],
    "number": [],
    "power_switch": [
        HCSwitchEntityDescription(
            key="switch_power_state",
            entity="BSH.Common.Setting.PowerState",
            device_class=SwitchDeviceClass.SWITCH,
        )
    ],
    "program": [
        HCSelectEntityDescription(
            key="select_program",
            entity="BSH.Common.Root.SelectedProgram",
            has_state_translation=True,
        )
    ],
    "select": [
        HCSelectEntityDescription(
            key="select_drying_assistant_all_programs",
            entity="Dishcare.Dishwasher.Setting.DryingAssistantAllPrograms",
            entity_category=EntityCategory.CONFIG,
            entity_registry_enabled_default=False,
            has_state_translation=True,
        ),
        HCSelectEntityDescription(
            key="select_hot_water",
            entity="Dishcare.Dishwasher.Setting.HotWater",
            entity_category=EntityCategory.CONFIG,
            entity_registry_enabled_default=False,
            has_state_translation=True,
        ),
        HCSelectEntityDescription(
            key="select_rinse_aid",
            entity="Dishcare.Dishwasher.Setting.RinseAid",
            entity_category=EntityCategory.CONFIG,
            entity_registry_enabled_default=False,
        ),
        HCSelectEntityDescription(
            key="select_sound_level_signal",
            entity="Dishcare.Dishwasher.Setting.SoundLevelSignal",
            entity_category=EntityCategory.CONFIG,
            entity_registry_enabled_default=False,
            has_state_translation=True,
        ),
        HCSelectEntityDescription(
            key="select_water_hardness",
            entity="Dishcare.Dishwasher.Setting.WaterHardness",
            entity_category=EntityCategory.CONFIG,
            entity_registry_enabled_default=False,
        ),
        HCSelectEntityDescription(
            key="select_remote_control_level",
            entity="BSH.Common.Setting.RemoteControlLevel",
            entity_category=EntityCategory.CONFIG,
            entity_registry_enabled_default=False,
            has_state_translation=True,
        ),
        HCSelectEntityDescription(
            key="select_sensitivity_turbidity",
            entity="Dishcare.Dishwasher.Setting.SensitivityTurbidity",
            entity_category=EntityCategory.CONFIG,
            entity_registry_enabled_default=False,
            has_state_translation=True,
        ),
        HCSelectEntityDescription(
            key="select_eco_as_default",
            entity="Dishcare.Dishwasher.Setting.EcoAsDefault",
            entity_category=EntityCategory.CONFIG,
            entity_registry_enabled_default=False,
            has_state_translation=True,
        ),
    ],
    "sensor": [
        HCSensorEntityDescription(
            key="sensor_remaining_program_time",
            entity="BSH.Common.Option.RemainingProgramTime",
            device_class=SensorDeviceClass.DURATION,
            native_unit_of_measurement=UnitOfTime.SECONDS,
            suggested_unit_of_measurement=UnitOfTime.HOURS,
            extra_attributes=[
                {
                    "name": "Is Estimated",
                    "entity": "BSH.Common.Option.RemainingProgramTimeIsEstimated",
                }
            ],
        ),
        HCSensorEntityDescription(
            key="sensor_program_progress",
            entity="BSH.Common.Option.ProgramProgress",
            native_unit_of_measurement=PERCENTAGE,
        ),
        HCSensorEntityDescription(
            key="sensor_operation_state",
            entity="BSH.Common.Status.OperationState",
            device_class=SensorDeviceClass.ENUM,
        ),
        HCSensorEntityDescription(
            key="sensor_program_phase",
            entity="Dishcare.Dishwasher.Status.ProgramPhase",
            device_class=SensorDeviceClass.ENUM,
        ),
        HCSensorEntityDescription(
            key="sensor_start_in",
            entity="BSH.Common.Option.StartInRelative",
            device_class=SensorDeviceClass.DURATION,
            native_unit_of_measurement=UnitOfTime.SECONDS,
            suggested_unit_of_measurement=UnitOfTime.HOURS,
        ),
        HCSensorEntityDescription(
            key="sensor_count_started",
            entity="BSH.Common.Status.Program.All.Count.Started",
            entity_category=EntityCategory.DIAGNOSTIC,
            entity_registry_enabled_default=False,
            state_class=SensorStateClass.TOTAL_INCREASING,
            extra_attributes=[
                {
                    "name": "Last Start",
                    "entity": "BSH.Common.Status.ProgramSessionSummary.Latest",
                    "value_fn": lambda entity: entity.value["start"],
                },
                {
                    "name": "Last End",
                    "entity": "BSH.Common.Status.ProgramSessionSummary.Latest",
                    "value_fn": lambda entity: entity.value["end"],
                },
            ],
        ),
        HCSensorEntityDescription(
            key="sensor_end_trigger",
            entity="BSH.Common.Status.ProgramRunDetail.EndTrigger",
            device_class=SensorDeviceClass.ENUM,
            entity_category=EntityCategory.DIAGNOSTIC,
            entity_registry_enabled_default=False,
            has_state_translation=True,
        ),
        HCSensorEntityDescription(
            key="sensor_interval_time_off",
            entity="Cooking.Hood.Setting.IntervalTimeOff",
            device_class=SensorDeviceClass.DURATION,
            native_unit_of_measurement=UnitOfTime.SECONDS,
        ),
        HCSensorEntityDescription(
            key="sensor_interval_time_on",
            entity="Cooking.Hood.Setting.IntervalTimeOn",
            device_class=SensorDeviceClass.DURATION,
            native_unit_of_measurement=UnitOfTime.SECONDS,
        ),
        HCSensorEntityDescription(
            key="sensor_delayed_shutoff_time",
            entity="Cooking.Hood.Setting.DelayedShutOffTime",
            device_class=SensorDeviceClass.DURATION,
            native_unit_of_measurement=UnitOfTime.SECONDS,
        ),
    ],
    "start_button": [
        HCButtonEntityDescription(
            key="button_start_program",
            entity="BSH.Common.Root.ActiveProgram",
        )
    ],
    "start_in": [
        HCNumberEntityDescription(
            key="select_start_in",
            entity="BSH.Common.Option.StartInRelative",
        )
    ],
    "switch": [
        HCSwitchEntityDescription(
            key="switch_hygiene_plus",
            entity="Dishcare.Dishwasher.Option.HygienePlus",
            device_class=SwitchDeviceClass.SWITCH,
        ),
        HCSwitchEntityDescription(
            key="switch_intensiv_zone",
            entity="Dishcare.Dishwasher.Option.IntensivZone",
            device_class=SwitchDeviceClass.SWITCH,
        ),
        HCSwitchEntityDescription(
            key="switch_vario_speed_plus",
            entity="Dishcare.Dishwasher.Option.VarioSpeedPlus",
            device_class=SwitchDeviceClass.SWITCH,
        ),
        HCSwitchEntityDescription(
            key="switch_silence_on_demand",
            entity="Dishcare.Dishwasher.Option.SilenceOnDemand",
            device_class=SwitchDeviceClass.SWITCH,
        ),
        HCSwitchEntityDescription(
            key="switch_brilliance_dry",
            entity="Dishcare.Dishwasher.Option.BrillianceDry",
            device_class=SwitchDeviceClass.SWITCH,
        ),
        HCSwitchEntityDescription(
            key="switch_extra_dry",
            entity="Dishcare.Dishwasher.Setting.ExtraDry",
            device_class=SwitchDeviceClass.SWITCH,
            entity_category=EntityCategory.CONFIG,
            entity_registry_enabled_default=False,
        ),
        HCSwitchEntityDescription(
            key="switch_speed_on_demand",
            entity="Dishcare.Dishwasher.Setting.SpeedOnDemand",
            device_class=SwitchDeviceClass.SWITCH,
            entity_category=EntityCategory.CONFIG,
            entity_registry_enabled_default=False,
        ),
        HCSwitchEntityDescription(
            key="switch_info_light",
            entity="Dishcare.Dishwasher.Setting.InfoLight",
            device_class=SwitchDeviceClass.SWITCH,
            entity_category=EntityCategory.CONFIG,
            entity_registry_enabled_default=False,
        ),
    ],
}
