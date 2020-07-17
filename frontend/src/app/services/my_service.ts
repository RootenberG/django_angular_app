import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable()
export class TaskService {

    constructor(private http: HttpClient) {
    }

    getTypes(): Observable<any[]> {
        const url = 'http://127.0.0.1:8000/api/';
        const params = new HttpParams();

        return this.http.get<any[]>(url, { params: params });
    }
}