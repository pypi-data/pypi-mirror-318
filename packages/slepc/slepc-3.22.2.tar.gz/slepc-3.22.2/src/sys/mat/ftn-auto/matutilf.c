#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* matutil.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepcsys.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define matcreatetile_ MATCREATETILE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define matcreatetile_ matcreatetile
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define matcreatevecsempty_ MATCREATEVECSEMPTY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define matcreatevecsempty_ matcreatevecsempty
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define matnormestimate_ MATNORMESTIMATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define matnormestimate_ matnormestimate
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  matcreatetile_(PetscScalar *a,Mat A,PetscScalar *b,Mat B,PetscScalar *c,Mat C,PetscScalar *d,Mat D,Mat *G, int *ierr)
{
CHKFORTRANNULLOBJECT(A);
CHKFORTRANNULLOBJECT(B);
CHKFORTRANNULLOBJECT(C);
CHKFORTRANNULLOBJECT(D);
PetscBool G_null = !*(void**) G ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(G);
*ierr = MatCreateTile(*a,
	(Mat)PetscToPointer((A) ),*b,
	(Mat)PetscToPointer((B) ),*c,
	(Mat)PetscToPointer((C) ),*d,
	(Mat)PetscToPointer((D) ),G);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! G_null && !*(void**) G) * (void **) G = (void *)-2;
}
SLEPC_EXTERN void  matcreatevecsempty_(Mat mat,Vec *right,Vec *left, int *ierr)
{
CHKFORTRANNULLOBJECT(mat);
PetscBool right_null = !*(void**) right ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(right);
PetscBool left_null = !*(void**) left ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(left);
*ierr = MatCreateVecsEmpty(
	(Mat)PetscToPointer((mat) ),right,left);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! right_null && !*(void**) right) * (void **) right = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! left_null && !*(void**) left) * (void **) left = (void *)-2;
}
SLEPC_EXTERN void  matnormestimate_(Mat A,Vec vrn,Vec w,PetscReal *nrm, int *ierr)
{
CHKFORTRANNULLOBJECT(A);
CHKFORTRANNULLOBJECT(vrn);
CHKFORTRANNULLOBJECT(w);
CHKFORTRANNULLREAL(nrm);
*ierr = MatNormEstimate(
	(Mat)PetscToPointer((A) ),
	(Vec)PetscToPointer((vrn) ),
	(Vec)PetscToPointer((w) ),nrm);
}
#if defined(__cplusplus)
}
#endif
