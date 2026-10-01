class InvalidPatientInfoError(Exception):
    pass


class Hospital:
    def register_patient(self, name, age):
        if not name.strip():
            raise InvalidPatientInfoError("Patient name cannot be empty.")
        if age <= 0:
            raise InvalidPatientInfoError("Patient age must be positive.")
        return "Patient registered: " + name


try:
    hospital = Hospital()
    print(hospital.register_patient("Sam", 30))
except InvalidPatientInfoError as error:
    print(error)