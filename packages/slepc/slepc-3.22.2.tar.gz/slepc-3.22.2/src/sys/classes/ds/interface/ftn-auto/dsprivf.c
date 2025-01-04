#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* dspriv.c */
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

#include "slepcds.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsviewmat_ DSVIEWMAT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsviewmat_ dsviewmat
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssetidentity_ DSSETIDENTITY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssetidentity_ dssetidentity
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsorthogonalize_ DSORTHOGONALIZE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsorthogonalize_ dsorthogonalize
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dspseudoorthogonalize_ DSPSEUDOORTHOGONALIZE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dspseudoorthogonalize_ dspseudoorthogonalize
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  dsviewmat_(DS ds,PetscViewer viewer,DSMatType *m, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLOBJECT(viewer);
*ierr = DSViewMat(
	(DS)PetscToPointer((ds) ),PetscPatchDefaultViewers((PetscViewer*)viewer),*m);
}
SLEPC_EXTERN void  dssetidentity_(DS ds,DSMatType *mat, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSSetIdentity(
	(DS)PetscToPointer((ds) ),*mat);
}
SLEPC_EXTERN void  dsorthogonalize_(DS ds,DSMatType *mat,PetscInt *cols,PetscInt *lindcols, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLINTEGER(lindcols);
*ierr = DSOrthogonalize(
	(DS)PetscToPointer((ds) ),*mat,*cols,lindcols);
}
SLEPC_EXTERN void  dspseudoorthogonalize_(DS ds,DSMatType *mat,PetscInt *cols,PetscReal s[],PetscInt *lindcols,PetscReal ns[], int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLREAL(s);
CHKFORTRANNULLINTEGER(lindcols);
CHKFORTRANNULLREAL(ns);
*ierr = DSPseudoOrthogonalize(
	(DS)PetscToPointer((ds) ),*mat,*cols,s,lindcols,ns);
}
#if defined(__cplusplus)
}
#endif
