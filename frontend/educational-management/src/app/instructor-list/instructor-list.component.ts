// import { Component, OnInit } from '@angular/core';
// import { InstructorService } from '../instructor.service';
// import { Instructor } from '../instructor.model';

// @Component({
//   selector: 'app-instructor-list',
//   templateUrl: './instructor-list.component.html',
//   styleUrls: ['./instructor-list.component.css'],
// })
// export class InstructorListComponent implements OnInit {
//   instructors: Instructor[] = [];

//   constructor(private instructorService: InstructorService) {}

//   ngOnInit(): void {
//     this.getInstructors();
//   }

//   getInstructors(): void {
//     this.instructorService.getInstructors()
//       .subscribe(instructors => {
//         this.instructors = instructors;
//       });
//   }

//   deleteInstructor(id: number): void {
//     if (confirm('Are you sure you want to delete this instructor?')) {
//       this.instructorService.deleteInstructor(id)
//         .subscribe(() => {
//           // Remove the deleted instructor from the list
//           this.instructors = this.instructors.filter(i => i.id !== id);
//         });
//     }
//   }
// }
// instructor-create.component.ts
import { Component } from '@angular/core';
import { InstructorService } from '../instructor.service';

@Component({
  selector: 'app-instructor-create',
  templateUrl: './instructor-create.component.html',
  styleUrls: ['./instructor-create.component.css']
})
export class InstructorCreateComponent {
  instructor: any = {}; // Instructor object to bind form inputs
  successMessage = '';
  errorMessage = '';

  constructor(private instructorService: InstructorService) {}

  onSubmit() {
    this.instructorService.createInstructor(this.instructor).subscribe(
      () => {
        this.successMessage = 'Instructor created successfully.';
        this.errorMessage = '';
      },
      (error) => {
        this.errorMessage = 'Error creating instructor. Please try again.';
        this.successMessage = '';
      }
    );
  }
}
