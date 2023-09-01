import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component'; // Import your components
import { InstructorComponent } from './instructor/instructor.component'; // Adjust the path as needed
import { InstructorCreateComponent } from './instructor-create/instructor-create.component';

const routes: Routes = [
    { path: '', component: DashboardComponent },
    { path: 'instructors', component: InstructorComponent },
    {path: 'instructors/create',component: InstructorCreateComponent}
    
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
