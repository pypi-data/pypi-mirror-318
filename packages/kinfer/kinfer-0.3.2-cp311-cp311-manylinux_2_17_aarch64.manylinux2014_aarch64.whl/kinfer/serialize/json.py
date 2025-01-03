"""Defines a serializer for JSON."""

import base64
from typing import Any, Mapping, Sequence

from kinfer import proto as P
from kinfer.serialize.base import (
    AudioFrameSerializer,
    CameraFrameSerializer,
    ImuSerializer,
    JointCommandsSerializer,
    JointPositionsSerializer,
    JointTorquesSerializer,
    JointVelocitiesSerializer,
    MultiSerializer,
    Serializer,
    StateTensorSerializer,
    TimestampSerializer,
    VectorCommandSerializer,
)
from kinfer.serialize.utils import (
    as_float,
    check_names_match,
    convert_angular_position,
    convert_angular_velocity,
    convert_torque,
)

Prim = str | int | float

JsonValue = Mapping[
    str,
    Prim
    | Sequence[Prim]
    | Sequence[Mapping[str, Prim]]
    | Mapping[str, Prim]
    | Mapping[str, Sequence[Prim]]
    | Mapping[str, Mapping[str, Prim]],
]


class JsonJointPositionsSerializer(JointPositionsSerializer[JsonValue]):
    def serialize_joint_positions(
        self: "JsonJointPositionsSerializer",
        schema: P.JointPositionsSchema,
        value: P.JointPositionsValue,
    ) -> dict[str, list[float]]:
        value_map = {v.joint_name: v for v in value.values}
        check_names_match("schema", schema.joint_names, "value", list(value_map.keys()))
        return {
            "positions": [
                convert_angular_position(value_map[name].value, value_map[name].unit, schema.unit)
                for name in schema.joint_names
            ]
        }

    def deserialize_joint_positions(
        self: "JsonJointPositionsSerializer",
        schema: P.JointPositionsSchema,
        value: JsonValue,
    ) -> P.JointPositionsValue:
        if "positions" not in value:
            raise ValueError("Key 'positions' not found in value")
        positions = value["positions"]
        if not isinstance(positions, list):
            raise ValueError("Key 'positions' must be a list")
        if len(positions) != len(schema.joint_names):
            raise ValueError(
                f"Shape of positions must match number of joint names: {len(positions)} != {len(schema.joint_names)}"
            )
        return P.JointPositionsValue(
            values=[
                P.JointPositionValue(joint_name=name, value=as_float(positions[i]), unit=schema.unit)
                for i, name in enumerate(schema.joint_names)
            ]
        )


class JsonJointVelocitiesSerializer(JointVelocitiesSerializer[JsonValue]):
    def serialize_joint_velocities(
        self: "JsonJointVelocitiesSerializer",
        schema: P.JointVelocitiesSchema,
        value: P.JointVelocitiesValue,
    ) -> dict[str, list[float]]:
        value_map = {v.joint_name: v for v in value.values}
        check_names_match("schema", schema.joint_names, "value", list(value_map.keys()))
        return {
            "velocities": [
                convert_angular_velocity(value_map[name].value, value_map[name].unit, schema.unit)
                for name in schema.joint_names
            ]
        }

    def deserialize_joint_velocities(
        self: "JsonJointVelocitiesSerializer",
        schema: P.JointVelocitiesSchema,
        value: JsonValue,
    ) -> P.JointVelocitiesValue:
        if "velocities" not in value:
            raise ValueError("Key 'velocities' not found in value")
        velocities = value["velocities"]
        if not isinstance(velocities, list):
            raise ValueError("Key 'velocities' must be a list")
        if len(velocities) != len(schema.joint_names):
            raise ValueError(
                f"Shape of velocities must match number of joint names: {len(velocities)} != {len(schema.joint_names)}"
            )
        return P.JointVelocitiesValue(
            values=[
                P.JointVelocityValue(joint_name=name, value=as_float(velocities[i]), unit=schema.unit)
                for i, name in enumerate(schema.joint_names)
            ]
        )


class JsonJointTorquesSerializer(JointTorquesSerializer[JsonValue]):
    def serialize_joint_torques(
        self: "JsonJointTorquesSerializer",
        schema: P.JointTorquesSchema,
        value: P.JointTorquesValue,
    ) -> dict[str, list[float]]:
        value_map = {v.joint_name: v for v in value.values}
        check_names_match("schema", schema.joint_names, "value", list(value_map.keys()))
        return {
            "torques": [
                convert_torque(value_map[name].value, value_map[name].unit, schema.unit) for name in schema.joint_names
            ]
        }

    def deserialize_joint_torques(
        self: "JsonJointTorquesSerializer",
        schema: P.JointTorquesSchema,
        value: JsonValue,
    ) -> P.JointTorquesValue:
        if "torques" not in value:
            raise ValueError("Key 'torques' not found in value")
        torques = value["torques"]
        if not isinstance(torques, list):
            raise ValueError("Key 'torques' must be a list")
        if len(torques) != len(schema.joint_names):
            raise ValueError(
                f"Shape of torques must match number of joint names: {len(torques)} != {len(schema.joint_names)}"
            )
        return P.JointTorquesValue(
            values=[
                P.JointTorqueValue(joint_name=name, value=as_float(torques[i]), unit=schema.unit)
                for i, name in enumerate(schema.joint_names)
            ]
        )


class JsonJointCommandsSerializer(JointCommandsSerializer[JsonValue]):
    def _convert_value_to_array(
        self: "JsonJointCommandsSerializer",
        value: P.JointCommandValue,
        schema: P.JointCommandsSchema,
    ) -> list[float]:
        return [
            convert_torque(value.torque, value.torque_unit, schema.torque_unit),
            convert_angular_velocity(value.velocity, value.velocity_unit, schema.velocity_unit),
            convert_angular_position(value.position, value.position_unit, schema.position_unit),
            float(value.kp),
            float(value.kd),
        ]

    def _convert_array_to_value(
        self: "JsonJointCommandsSerializer",
        values: Any,  # noqa: ANN401
        schema: P.JointCommandsSchema,
        name: str,
    ) -> P.JointCommandValue:
        if not isinstance(values, list):
            raise ValueError("Value must be a list")
        if len(values) != 5:
            raise ValueError(f"Shape of command must match number of joint commands: {len(values)} != 5")
        return P.JointCommandValue(
            joint_name=name,
            torque=float(values[0]),
            velocity=float(values[1]),
            position=float(values[2]),
            kp=float(values[3]),
            kd=float(values[4]),
            torque_unit=schema.torque_unit,
            velocity_unit=schema.velocity_unit,
            position_unit=schema.position_unit,
        )

    def serialize_joint_commands(
        self: "JsonJointCommandsSerializer",
        schema: P.JointCommandsSchema,
        value: P.JointCommandsValue,
    ) -> dict[str, dict[str, list[float]]]:
        value_map = {v.joint_name: v for v in value.values}
        check_names_match("schema", schema.joint_names, "value", list(value_map.keys()))
        return {
            "commands": {name: self._convert_value_to_array(value_map[name], schema) for name in schema.joint_names}
        }

    def deserialize_joint_commands(
        self: "JsonJointCommandsSerializer",
        schema: P.JointCommandsSchema,
        value: JsonValue,
    ) -> P.JointCommandsValue:
        if "commands" not in value:
            raise ValueError("Key 'commands' not found in value")
        commands = value["commands"]
        if not isinstance(commands, dict):
            raise ValueError("Key 'commands' must be a dictionary")
        check_names_match("schema", schema.joint_names, "value", list(commands.keys()))
        return P.JointCommandsValue(
            values=[self._convert_array_to_value(commands[name], schema, name) for name in schema.joint_names]
        )


class JsonCameraFrameSerializer(CameraFrameSerializer[JsonValue]):
    def serialize_camera_frame(
        self: "JsonCameraFrameSerializer",
        schema: P.CameraFrameSchema,
        value: P.CameraFrameValue,
    ) -> dict[str, str]:
        return {"data": base64.b64encode(value.data).decode("utf-8")}

    def deserialize_camera_frame(
        self: "JsonCameraFrameSerializer",
        schema: P.CameraFrameSchema,
        value: JsonValue,
    ) -> P.CameraFrameValue:
        if "data" not in value:
            raise ValueError("Key 'data' not found in value")
        data = value["data"]
        if not isinstance(data, str):
            raise ValueError("Key 'data' must be a string")
        return P.CameraFrameValue(data=base64.b64decode(data))


class JsonAudioFrameSerializer(AudioFrameSerializer[JsonValue]):
    def serialize_audio_frame(
        self: "JsonAudioFrameSerializer",
        schema: P.AudioFrameSchema,
        value: P.AudioFrameValue,
    ) -> dict[str, str]:
        return {"data": base64.b64encode(value.data).decode("utf-8")}

    def deserialize_audio_frame(
        self: "JsonAudioFrameSerializer",
        schema: P.AudioFrameSchema,
        value: JsonValue,
    ) -> P.AudioFrameValue:
        if "data" not in value:
            raise ValueError("Key 'data' not found in value")
        data = value["data"]
        if not isinstance(data, str):
            raise ValueError("Key 'data' must be a string")
        return P.AudioFrameValue(data=base64.b64decode(data))


class JsonImuSerializer(ImuSerializer[JsonValue]):
    def serialize_imu(
        self: "JsonImuSerializer",
        schema: P.ImuSchema,
        value: P.ImuValue,
    ) -> dict[str, list[float]]:
        data: dict[str, list[float]] = {}
        if schema.use_accelerometer:
            data["linear_acceleration"] = [
                value.linear_acceleration.x,
                value.linear_acceleration.y,
                value.linear_acceleration.z,
            ]
        if schema.use_gyroscope:
            data["angular_velocity"] = [
                value.angular_velocity.x,
                value.angular_velocity.y,
                value.angular_velocity.z,
            ]
        if schema.use_magnetometer:
            data["magnetic_field"] = [
                value.magnetic_field.x,
                value.magnetic_field.y,
                value.magnetic_field.z,
            ]
        return data

    def deserialize_imu(
        self: "JsonImuSerializer",
        schema: P.ImuSchema,
        value: JsonValue,
    ) -> P.ImuValue:
        imu_value = P.ImuValue()
        if schema.use_accelerometer:
            if not isinstance(linear_acceleration := value["linear_acceleration"], list):
                raise ValueError("Key 'linear_acceleration' must be a list")
            x, y, z = linear_acceleration
            imu_value.linear_acceleration.x = as_float(x)
            imu_value.linear_acceleration.y = as_float(y)
            imu_value.linear_acceleration.z = as_float(z)
        if schema.use_gyroscope:
            if not isinstance(angular_velocity := value["angular_velocity"], list):
                raise ValueError("Key 'angular_velocity' must be a list")
            x, y, z = angular_velocity
            imu_value.angular_velocity.x = as_float(x)
            imu_value.angular_velocity.y = as_float(y)
            imu_value.angular_velocity.z = as_float(z)
        if schema.use_magnetometer:
            if not isinstance(magnetic_field := value["magnetic_field"], list):
                raise ValueError("Key 'magnetic_field' must be a list")
            x, y, z = magnetic_field
            imu_value.magnetic_field.x = as_float(x)
            imu_value.magnetic_field.y = as_float(y)
            imu_value.magnetic_field.z = as_float(z)
        return imu_value


class JsonTimestampSerializer(TimestampSerializer[JsonValue]):
    def serialize_timestamp(
        self: "JsonTimestampSerializer",
        schema: P.TimestampSchema,
        value: P.TimestampValue,
    ) -> dict[str, int]:
        return {"seconds": value.seconds, "nanos": value.nanos}

    def deserialize_timestamp(
        self: "JsonTimestampSerializer",
        schema: P.TimestampSchema,
        value: JsonValue,
    ) -> P.TimestampValue:
        if "seconds" not in value or "nanos" not in value:
            raise ValueError("Key 'seconds' or 'nanos' not found in value")
        seconds = value["seconds"]
        nanos = value["nanos"]
        if not isinstance(seconds, int) or not isinstance(nanos, int):
            raise ValueError("Key 'seconds' and 'nanos' must be integers")
        return P.TimestampValue(seconds=seconds, nanos=nanos)


class JsonVectorCommandSerializer(VectorCommandSerializer[JsonValue]):
    def serialize_vector_command(
        self: "JsonVectorCommandSerializer",
        schema: P.VectorCommandSchema,
        value: P.VectorCommandValue,
    ) -> dict[str, list[float]]:
        return {"values": list(value.values)}

    def deserialize_vector_command(
        self: "JsonVectorCommandSerializer",
        schema: P.VectorCommandSchema,
        value: JsonValue,
    ) -> P.VectorCommandValue:
        if "values" not in value:
            raise ValueError("Key 'values' not found in value")
        values = value["values"]
        if not isinstance(values, list):
            raise ValueError("Key 'values' must be a list")
        if len(values) != schema.dimensions:
            raise ValueError(f"Length of list must match number of dimensions: {len(values)} != {schema.dimensions}")
        return P.VectorCommandValue(values=[as_float(v) for v in values])


class JsonStateTensorSerializer(StateTensorSerializer[JsonValue]):
    def serialize_state_tensor(
        self: "JsonStateTensorSerializer",
        schema: P.StateTensorSchema,
        value: P.StateTensorValue,
    ) -> dict[str, str]:
        return {"data": base64.b64encode(value.data).decode("utf-8")}

    def deserialize_state_tensor(
        self: "JsonStateTensorSerializer",
        schema: P.StateTensorSchema,
        value: JsonValue,
    ) -> P.StateTensorValue:
        if "data" not in value:
            raise ValueError("Key 'data' not found in value")
        data = value["data"]
        if not isinstance(data, str):
            raise ValueError("Key 'data' must be a string")
        return P.StateTensorValue(data=base64.b64decode(data))


class JsonSerializer(
    JsonJointPositionsSerializer,
    JsonJointVelocitiesSerializer,
    JsonJointTorquesSerializer,
    JsonJointCommandsSerializer,
    JsonCameraFrameSerializer,
    JsonAudioFrameSerializer,
    JsonImuSerializer,
    JsonTimestampSerializer,
    JsonVectorCommandSerializer,
    JsonStateTensorSerializer,
    Serializer[JsonValue],
):
    def __init__(self: "JsonSerializer", schema: P.ValueSchema) -> None:
        Serializer.__init__(self, schema=schema)


class JsonMultiSerializer(MultiSerializer[JsonValue]):
    def __init__(self: "JsonMultiSerializer", schema: P.IOSchema) -> None:
        super().__init__([JsonSerializer(schema=s) for s in schema.values])
