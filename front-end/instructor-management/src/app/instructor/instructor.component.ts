// import { Component, OnInit } from '@angular/core';
// import { InstructorService } from '../instructor.service'; // Adjust the path as needed


// @Component({
//   selector: 'app-instructor',
//   templateUrl: './instructor.component.html',
//   styleUrls: ['./instructor.component.css']
// })
// export class InstructorComponent implements OnInit {

//   "instructors": any[]; // Define a variable to store the fetched instructors

//   constructor(private instructorService: InstructorService) { }

//   ngOnInit(): void {
//     this.loadInstructors(); // Load instructors when the component initializes
//   }

//   loadInstructors(): void {
//     this.instructorService.getInstructors()
//       .subscribe(
//         (data) => {
//           this.instructors = data;
//         },
//         (error) => {
//           console.error('Error fetching instructors:', error);
//         }
//       );
//   }

//   // Other CRUD methods...

// }
// instructor.component.ts

import { Component, OnInit } from '@angular/core';
import { InstructorService } from '../instructor.service';
import { Instructor } from './instructor.model'; // Adjust the path as needed


@Component({
  selector: 'app-instructor',
  templateUrl: './instructor.component.html',
  styleUrls: ['./instructor.component.css']
})
export class InstructorComponent implements OnInit {
  instructors: Instructor[] = []// Specify the type as Instructor[]

  constructor(private instructorService: InstructorService) { }

  ngOnInit(): void {
    this.loadInstructors();
  }
  loadInstructors(): void {
    this.instructorService.getInstructors()
      .subscribe(
        (data) => {
          if (data && data.instructors) {
            this.instructors = data.instructors as Instructor[]; // Type assertion
          } else {
            console.error('Invalid API response:', data);
          }
        },
        (error) => {
          console.error('Error fetching instructors:', error);
        }
      );
  }
  

  // Implement other CRUD methods here (create, update, delete)
}
