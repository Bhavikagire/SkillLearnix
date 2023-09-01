export class Instructor {
    id: number;
    name: string = ''; // Initialize with an empty string
    gender: string;
    date_of_birth: string;
    department: string;
    email: string;
    contact_number: string;
  
    constructor(id: number, name: string, gender: string, date_of_birth: string, department: string, email: string, contact_number: string) {
      this.id = id;
      this.name = name;
      this.gender = gender;
      this.date_of_birth = date_of_birth;
      this.department = department;
      this.email = email;
      this.contact_number = contact_number;
    }
  }
  