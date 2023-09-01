export class Instructor {
    id: number = 0;
    name: string = '';
    gender: string = '';
    date_of_birth: string = '';
    department: string = '';
    email: string = '';
    contact_number: string = '';
  
    constructor(data: Partial<Instructor>) {
      Object.assign(this, data);
    }
  }
  