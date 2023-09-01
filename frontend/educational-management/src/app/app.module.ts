import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { InstructorCreateComponent } from './instructor-create/instructor-create.component';

const appRoutes: Routes = [
  { path: 'instructors/create', component: InstructorCreateComponent },
  { path: '', redirectTo: '/instructors', pathMatch: 'full' },
  { path: '**', redirectTo: '/instructors' },
];

@NgModule({
  declarations: [
    AppComponent,
    InstructorCreateComponent,
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(appRoutes),
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
